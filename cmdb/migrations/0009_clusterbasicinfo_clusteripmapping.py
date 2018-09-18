# Generated by Django 2.1.1 on 2018-09-14 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0008_auto_20180911_2232'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClusterBasicInfo',
            fields=[
                ('cluster_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cluster_name', models.CharField(max_length=16)),
                ('cluster_type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CLusterIpMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=16)),
                ('cluster_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.ClusterBasicInfo')),
            ],
        ),
    ]
