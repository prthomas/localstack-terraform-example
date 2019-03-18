"""
Module to run tests for example
"""
import os
import unittest

import botocore

from localstack.constants import DEFAULT_SERVICE_PORTS

from boto3_s3 import Boto3S3
from example import get_boto3_resource
from example import s3_to_dynamodb


class TestExample(unittest.TestCase):
    """
    TestExample class includes tests for testing implemented code
        This spins up a localstack process to test AWS services
    """
    @classmethod
    def setUpClass(cls):
        cls.startservices = ['s3', 'dynamodb']
        os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'
        for service in cls.startservices:
            os.environ['{}_endpoint_url'.format(service)] = ''.join([
                'http://',
                '127.0.0.1:',
                str(DEFAULT_SERVICE_PORTS[service])])

    def test_s3_to_dynamodb(self):
        """Test s3_to_dynamodb function"""
        boto3s3 = Boto3S3()
        s3rsrc = boto3s3.rsrc
        s3bucket = s3rsrc.Bucket('bucket_for_trigger')
        for obj in s3bucket.objects.all():
            print(obj)
        s3obj = s3rsrc.Object('bucket_for_trigger', 'gdata.csv')
        self.assertEqual(s3obj.content_length, 1410)
        s3_to_dynamodb('bucket_for_trigger', 'gdata.csv')
        dynamodb = get_boto3_resource('dynamodb')
        dynamotbl = dynamodb.Table('gdata')
        self.assertEqual(dynamotbl.item_count, 30)
        self.assertEqual(
            dynamotbl.get_item(
                Key={
                    'sales': '147327000000',
                    'business': '44000'
                },
                AttributesToGet=['line']
            )['Item']['line'],
            'Seasonally Adjusted,44000,1992.03,147327000000')
        self.assertFalse('Item' in dynamotbl.get_item(
            Key={
                'sales': 'notpresentsale',
                'business': '44000'
            },
            AttributesToGet=['line']
        ))

if __name__ == '__main__':
    unittest.main()
