import os
import json

from scans import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')
from scans import Response


def worker(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    item = table.get_item(
        Key={
            #'id': event['pathParameters']['id']
            #'id': REPLACE_WITH_ID_FROM_UPDATE_STREAM_EVENT
        }
    )

    # Use this to give us a signal it's working
    logger.info('{0}:{1}:{2}'.format(
        item["target"], item["port"], REPLACE_WITH_ID_FROM_UPDATE_STREAM_EVENT))

    # TODO: Add real scan logic here to populate scan, probably via a scan-engine
    #  class implemented in Python instead of Ruby
    #  https://github.com/mozilla/ssh_scan/blob/master/lib/ssh_scan/scan_engine.rb
    scan = {
        'target': 'ssh.mozilla.com',
        'port': 'ssh.mozilla.com',
        'foo': 'bar'
    }

    table.update_item(
        Key={
            #'id': event['pathParameters']['id']
            #'id': REPLACE_WITH_ID_FROM_UPDATE_STREAM_EVENT
        }
        UpdateExpression='SET scan = :a, status = :b',
        ExpressionAttributeValues={
            ':a': scan,
            ':b': "COMPLETE"
        }
    )
