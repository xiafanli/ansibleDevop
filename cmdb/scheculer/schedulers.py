from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
import time
import requests
from rest_framework import status

from cmdb.common import options
from cmdb.models import HostBasicInfo
from util.field import HostInfoFields
import logging

logger = logging.getLogger(__name__)

jobstores = {
    'django': DjangoJobStore(),
    #'default': SQLAlchemyJobStore(url='sqlite:///db.sqlite3')
}

executors = {
    'default': ThreadPoolExecutor(5),
    'processpool': ProcessPoolExecutor(2)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}


class JobScheduler(object):
    def __init__(self):
        self.scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)
        register_events(self.scheduler)

    def start(self):
        self.scheduler.start()

    def add_job(self, job_func, job_id, interval_minutes):
        self.scheduler.add_job(job_func, 'interval', minutes=interval_minutes, id=job_id)


class CollectHostInfo(object):
    def __init__(self, idcinfo_ip):
        self.idcinfo_url = 'http://%s/server/ajax/search/' % idcinfo_ip


    def update_host_info_from_idc(self):
        all_hosts_queryset = HostBasicInfo.objects.all()
        update_fields = [HostInfoFields.F_MANAGER_IP, HostInfoFields.F_RACK_ID,
                         HostInfoFields.F_MODEL, HostInfoFields.F_ROOM]
        for hostinfo in all_hosts_queryset:
            if hostinfo.machine_type == 'physical':
                manager_ip, rack, model, room = self.get_host_info_by_sn(hostinfo.serial)
                if (hostinfo.manager_ip != manager_ip and manager_ip != options.DEFAULT_MANAGER_IP_ADDRESS) \
                        or len(hostinfo.manager_ip.strip()) == 0:
                    hostinfo.manager_ip = manager_ip
                hostinfo.rack_id = rack
                hostinfo.model = model
                hostinfo.room = room
                hostinfo.save(update_fields=update_fields)
                print(hostinfo.ip_address)

    def get_host_info_by_sn(self, serial_no):
        payload = {'keywords': serial_no}
        try:
            r = requests.get(self.idcinfo_url, params=payload)
            logger.info("request: %s" % r.url)
            if 'r' in dir() and r.status_code == status.HTTP_200_OK:
                data = r.json().get('data')[0]
                if len(data) == 0:
                    print("cannot query data")

                else:
                    rack_1 = data.get('racks')[0]
                    rack_unit_startat = rack_1.get('unit_startat')
                    rack_unit_endat = rack_1.get('unit_endat')
                    rack_name = rack_1.get('rack')
                    rack = '%s,%s-%s' % (rack_name, rack_unit_startat, rack_unit_endat)

                    manager_ip = data.get('m_ip')
                    model = data.get('model')
                    room = data.get('room')
                    return manager_ip, rack, model, room
        except Exception as ex:
            print(ex.__str__())

        return None



