"""This module implements function s3_to_dynamodb"""
from boto3_resource import get_boto3_resource
from boto3_s3 import Boto3S3

def lambda_func(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        s3_to_dynamodb(bucket, key)


def s3_to_dynamodb(bucket, key):
    """
    Function to read s3 file, convert it to an `item`, and load into dynamodb
    """
    s3obj = Boto3S3()
    dynamotbl = get_boto3_resource('dynamodb').Table('gdata')
    with dynamotbl.batch_writer() as gdatawriter:
        with s3obj.stream(bucket, key) as filestream:
            for rline in filestream:
                line = rline.strip()
                cols = line.split(',')
                gdatawriter.put_item({
                    'sales': cols[3],
                    'business': cols[1],
                    'line': line
                })
