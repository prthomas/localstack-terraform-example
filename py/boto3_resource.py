"""This module implements function get_boto3_resource"""
import os
import boto3


def get_boto3_resource(service):
    """get boto3 resource, check for test endpoint url form env var"""
    endpointurl = os.environ.get("{}_endpoint_url".format(service))
    if endpointurl:
        session = boto3.Session(profile_name='mock')
        return session.resource(service, endpoint_url=endpointurl)

    return boto3.resource(service)
