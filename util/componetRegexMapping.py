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
    "org.apache.spark.deploy.history.HistoryServer": "HistoryServer",
    "org.elasticsearch.bootstrap.Elasticsearch": "Elasticsearch",
    "kafka.Kafka": "Kafka",
    "org.apache.hadoop.hbase.master.HMaster": "Hmaster",
    "org.apache.hadoop.hbase.regionserver.HRegionServer": "HRegionServer"
    }

COMPONENT_LIB_PATH = {
    'Kafka': ['/bankapp/bankdplyop/kafka/libs', 'bankapp/kafka/kafka/libs', '/home/bankdplyop/kafka/libs',
              '/wls/kafka/kafka_2.11-0.10.0.1/libs', '/home/kafka/kafka/libs'],
    'Zookeeper': ['/usr/lib/zookeeper', '/home/zookeeper/zookeeper', '/wls/kafka/zookeeper-3.4.6',
                  '/bankapp/zookeeper/zookeeper']
}

COMPONENT_LIB_NAME_REGEX = {
    'Kafka': '^kafka_2.11-([\d+.]+).jar$',
    'Zookeeper': '^zookeeper-([\d+\-cdh.]+).jar$'
}