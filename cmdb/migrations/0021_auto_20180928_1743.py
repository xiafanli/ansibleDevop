# Generated by Django 2.1.1 on 2018-09-28 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0020_auto_20180928_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clusterbasicinfo',
            name='host_info',
            field=models.ManyToManyField(through='cmdb.ClusterHostMapping', to='cmdb.HostBasicInfo'),
        ),
    ]
