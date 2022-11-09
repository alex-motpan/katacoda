#!/usr/bin/python3
import boto3
from pprint import pprint
from botocore.config import Config
import json
import sys



cluster= sys.argv[1]
# print (cluster)
my_config = Config(region_name = 'eu-west-1')

client = boto3.client('rds', config=my_config)

response = client.describe_db_clusters(
    DBClusterIdentifier= cluster
)
d= {}
d["data"] = [] 
members = response['DBClusters'][0]['DBClusterMembers']
for member in members:
    if member['IsClusterWriter'] :
        role = "writer"
    else :
        role = "reader"
    d["data"].append(
        {
            "{#DBINSTANCE}" : member['DBInstanceIdentifier'],
            "{#DBROLE}" : role,
            "{#CLUSTER}" : cluster
        }
    )
print (json.dumps(d))