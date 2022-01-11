import boto3
import yaml
import os

# this bit tries to safe load the YAML config file, and set it as a variable
with open("config.yml", "r") as stream:
    try:
        cfg = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

# since boto3 doesn't like it when I try to give it the whole config, here I break it out into bite-sized pieces
INSTANCE_TYPE = cfg['server']['instance_type']
AWS_REGION = cfg['server']['aws_region']
AMI_TYPE = cfg['server']['ami_type']
ARCHITECTURE = cfg['server']['architecture']
ROOT_DEVICE_TYPE = cfg['server']['root_device_type']
VIRTUALIZATION_TYPE = cfg['server']['virtualization_type']
MIN_COUNT = cfg['server']['min_count']
MAX_COUNT = cfg['server']['max_count']
VOLUMES = cfg['server']['volumes']
USERS = cfg['server']['users']
#print(VOLUMES)

EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
# I tried to programmatically pick an AMI by filtering the list, lost my patience.
AMI_ID = 'ami-03af6a70ccd8cb578'
USERDATA_SCRIPT = '''
    #!/bin/bash
    mkfs -t ext4 /dev/xvdf
    mkdir data
    mount /dev/xvdf /data
    chmod 777 /data
    adduser user1 -p ""
    adduser user2 -p ""
    
'''

instances = EC2_RESOURCE.create_instances(
    InstanceType = INSTANCE_TYPE,
    MinCount = MIN_COUNT,
    MaxCount = MAX_COUNT,
    ImageId=AMI_ID,
    KeyName="Admin",
    UserData=USERDATA_SCRIPT,
    BlockDeviceMappings=VOLUMES,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Fetch Rewards Challenge Instance'
                },
            ]
        },
    ]
)

for instance in instances:
    print(f'EC2 instance "{instance.id}" has been launched')
    
    instance.wait_until_running()
    print(f'EC2 instance "{instance.id}" has been started')