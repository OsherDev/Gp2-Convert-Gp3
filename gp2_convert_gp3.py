import boto3
import botocore

client = boto3.client('ec2')


def lambda_handler(event, context):
    response = client.describe_volumes()
    for result in response['Volumes']:
        VolumeId = result['VolumeId']
        VolumeType = result['VolumeType']
        Size = result['Size']
        IOP = result['Iops']
    try:
        if Size < 1000 and IOP < 3000 and (VolumeType  == 'gp2'):
            modify = client.modify_volume(VolumeId=VolumeId,VolumeType='gp3')
            print(f"{VolumeId} chnaged to gp3")
        else: 
            print(f"{VolumeId} does not fit criteria")
    except botocore.exceptions.ClientError as error:
        print(error)
