from scans import Response
import os
import json

from scans import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])


def worker(event, context):
    for record in event["Records"]:
        if not record["eventName"] == "INSERT":
            continue

        item = record["dynamodb"]["NewImage"]
        scan_id = item["id"]["S"]
        target = item["target"]["S"]
        port = item["target"]["I"]

        # Use this to give us a signal it's working
        logger.info('{0} {1}:{2}'.format(
            scan_id, target, port))

        # TODO: Add real scan logic here to populate scan var, probably via a scan-engine
        #  class implemented in Python instead of Ruby
        #  https://github.com/mozilla/ssh_scan/blob/master/lib/ssh_scan/scan_engine.rb
        # In the mean time, we'll manually curate for the sake of example/testing
        scan = {
            'target': target,
            'port': port,
            'foo': 'bar'
        }

        # Add scan results to the item
        table.update_item(
            Key={
                'id': scan_id
            }
            UpdateExpression='SET scan = :r',
            ExpressionAttributeValues={
                ':r': scan,
            }
        )
