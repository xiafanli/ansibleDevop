component_mapping = {
    "org.apache.zookeeper.server.quorum.QuorumPeerMain": "Zookeeper",
    "org.apache.hadoop.hdfs.qjournal.server.JournalNode": "JournalNode",
    "org.apache.hadoop.hdfs.tools.DFSZKFailoverController": "DFSZKFailoverController",
    "org.apache.hadoop.hdfs.server.datanode.DataNode": "DataNode",
    "org.apache.sentry.SentryMain": "SentryMain",
    "org.apache.hadoop.yarn.server.resourcemanager.ResourceManager": "ResourceManager",
    "org.apache.hadoop.mapreduce.v2.hs.JobHistoryServer": "JobHistoryServer",
    "org.apache.hadoop.hdfs.server.namenode.NameNode": "NameNode",
    "org.apache.hive.service.server.HiveServer2": "HiveServer2",
    "org.apache.hadoop.hive.metastore.HiveMetaStore": "HiveMetaStore",
    "_JobHistory/.*org.apache.spark.deploy.history.HistoryServer": "HistoryServer",
    "SPARK_YARN_HISTORY_SERVER": "HistoryServer",
    "_JobHistory2x/.*org.apache.spark.deploy.history.HistoryServer": "HistoryServer2x",
    "org.apache.spark.sql.hive.thriftserver.om.ha.HiveThriftServer2Shell": "JDBCServer",
    "org.apache.spark.sql.hive.thriftserver.HiveThriftProxyServer2": "JDBCServer2x",
    "org.elasticsearch.bootstrap.Elasticsearch": "Elasticsearch",
    "kafka.Kafka": "Kafka",
    "org.apache.hadoop.hbase.master.HMaster": "HMaster",
    "org.apache.hadoop.hbase.regionserver.HRegionServer": "HRegionServer"
    }

COMPONENT_LIB_PATH = {
    'Kafka': ['/bankapp/bankdplyop/kafka/libs', 'bankapp/kafka/kafka/libs', '/home/bankdplyop/kafka/libs',
              '/wls/kafka/kafka_2.11-0.10.0.1/libs', '/home/kafka/kafka/libs'],
    'Zookeeper': ['/usr/lib/zookeeper', '/home/zookeeper/zookeeper', '/wls/kafka/zookeeper-3.4.6',
                  '/bankapp/zookeeper/zookeeper', '/opt/cloudera/parcels/CDH/lib/zookeeper'],
    'NameNode': ['/opt/cloudera/parcels/CDH/lib/hadoop-hdfs', '/usr/lib/hadoop-hdfs',
                 '/opt/huawei/Bigdata/hadoop/hadoop/share/hadoop/hdfs',
                 '/opt/huawei/Bigdata/FusionInsight/FusionInsight-Hadoop-*/hadoop/share/hadoop/hdfs'],
    'DataNode': ['/opt/cloudera/parcels/CDH/lib/hadoop-hdfs', '/usr/lib/hadoop-hdfs',
                 '/opt/huawei/Bigdata/hadoop/hadoop/share/hadoop/hdfs',
                 '/opt/huawei/Bigdata/FusionInsight/FusionInsight-Hadoop-*/hadoop/share/hadoop/hdfs'],
    'JournalNode': ['/opt/cloudera/parcels/CDH/lib/hadoop-hdfs', '/usr/lib/hadoop-hdfs',
                    '/opt/huawei/Bigdata/hadoop/hadoop/share/hadoop/hdfs',
                    '/opt/huawei/Bigdata/FusionInsight/FusionInsight-Hadoop-*/hadoop/share/hadoop/hdfs'],
    'DFSZKFailoverController': ['/opt/cloudera/parcels/CDH/lib/hadoop-hdfs', '/usr/lib/hadoop-hdfs',
                                '/opt/huawei/Bigdata/hadoop/hadoop/share/hadoop/hdfs',
                                '/opt/huawei/Bigdata/FusionInsight/FusionInsight-Hadoop-*/hadoop/share/hadoop/hdfs'],
    'ResourceManager': ['/opt/cloudera/parcels/CDH/lib/hadoop-yarn', '/usr/lib/hadoop-yarn',
                        '/opt/huawei/Bigdata/hadoop/hadoop/share/hadoop/yarn',
                        '/opt/huawei/Bigdata/FusionInsight/FusionInsight-Hadoop-*/hadoop/share/hadoop/yarn'],
    'NodeManager': ['/opt/cloudera/parcels/CDH/lib/hadoop-yarn', '/usr/lib/hadoop-yarn',
                    '/opt/huawei/Bigdata/hadoop/hadoop/share/hadoop/yarn',
                    '/opt/huawei/Bigdata/FusionInsight/FusionInsight-Hadoop-*/hadoop/share/hadoop/yarn'],
    'JobHistoryServer': ['/opt/cloudera/parcels/CDH/lib/hadoop-yarn', '/usr/lib/hadoop-yarn',
                         '/opt/huawei/Bigdata/hadoop/hadoop/share/hadoop/hdfs',
                         '/opt/huawei/Bigdata/FusionInsight/FusionInsight-Hadoop-*/hadoop/share/hadoop/hdfs'],
    'HMaster': ['/opt/cloudera/parcels/CDH/lib/hbase', '/usr/lib/hbase',
                '/opt/huawei/Bigdata/FusionInsight_Current/*_HMaster/install/hbase/lib',
                '/opt/huawei/Bigdata/FusionInsight/FusionInsight-HBase-*/hbase/lib'],
    'HRegionServer': ['/opt/cloudera/parcels/CDH/lib/hbase', '/usr/lib/hbase',
                      '/opt/huawei/Bigdata/FusionInsight_Current/*_HMaster/install/hbase/lib',
                      '/opt/huawei/Bigdata/FusionInsight/FusionInsight-HBase-*/hbase/lib'],
    'HiveServer2': ['/opt/cloudera/parcels/CDH/lib/hive', '/usr/lib/hive',
                    '/opt/huawei/Bigdata/FusionInsight_Current/*_HiveServer/install/hive-*/lib',
                    '/opt/huawei/Bigdata/FusionInsight/FusionInsight-Hive-*/hive-*/lib'],
    'HiveMetaStore': ['/opt/cloudera/parcels/CDH/lib/hive', '/usr/lib/hive',
                      '/opt/huawei/Bigdata/FusionInsight_Current/*_MetaStore/install/hive-*/lib',
                      '/opt/huawei/Bigdata/FusionInsight/FusionInsight-Hive-*/hive-*/lib'],
    'HistoryServer': ['/opt/cloudera/parcels/CDH/lib/spark/lib',
                      '/opt/huawei/Bigdata/FusionInsight_Current/*_JobHistory/install/spark/lib'],
    'JDBCServer': ['/opt/huawei/Bigdata/FusionInsight_Current/*_JDBCServer/install/spark/lib'],
    'HistoryServer2x': ['/opt/huawei/Bigdata/FusionInsight_Current/*_JobHistory2x/install/spark/jars'],
    'JDBCServer2x': ['/opt/huawei/Bigdata/FusionInsight_Current/*_JDBCServer2x/install/spark/jars'],
    'SentryMain': ['/opt/cloudera/parcels/CDH/lib/sentry/lib']

}

COMPONENT_LIB_NAME_REGEX = {
    'Kafka': '^kafka_([\d+\-kafka.]+).jar$',
    'Zookeeper': '^zookeeper-([\d+\-cdh.]+).jar$',
    'NameNode': '^hadoop-hdfs-([\d+\-cdh.]+).jar',
    'DataNode': '^hadoop-hdfs-([\d+\-cdh.]+).jar',
    'JournalNode': '^hadoop-hdfs-([\d+\-cdh.]+).jar',
    'DFSZKFailoverController': '^hadoop-hdfs-([\d+\-cdh.]+).jar$',
    'ResourceManager': '^hadoop-yarn-common-([\d+\-cdh.]+).jar$',
    'NodeManager': '^hadoop-yarn-common-([\d+\-cdh.]+).jar$',
    'JobHistoryServer': '^hadoop-yarn-common-([\d+\-cdh.]+).jar$',
    'HMaster': '^hbase-server-([\d+\-cdh.]+).jar$',
    'HRegionServer': '^hbase-server-([\d+\-cdh.]+).jar$',
    'HiveServer2': '^hive-service-([\d+\-cdh.]+).jar$',
    'HiveMetaStore': '^hive-metastore-([\d+\-cdh.]+).jar$',
    'SentryMain': '^sentry-core-common-([\d+\-cdh.]+).jar$',
    'HistoryServer': '^spark-core_([\d+\-.]+).jar$|^spark-assembly-([\d+\-cdh.]+)-hadoop.*jar$',
    'JDBCServer': '^spark-core_([\d+\-.]+).jar$',
    'HistoryServer2x': '^spark-core_([\d+\-.]+).jar$',
    'JDBCServer2x': '^spark-core_([\d+\-.]+).jar$'
}