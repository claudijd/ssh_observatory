import os
import json

from scans import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')
from scans import Response


def worker(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # Example event to play with
    # {
    #     "Records": [
    #         {
    #             "eventID": "1",
    #             "eventVersion": "1.0",
    #             "dynamodb": {
    #                 "Keys": {
    #                     "id": {
    #                         "S": "a88cb45c-0ac1-47b3-865b-a92f05d7612b"
    #                     }
    #                 },
    #                 "NewImage": {
    #                     "target": {
    #                         "S": "ssh.mozilla.com"
    #                     },
    #                     "port": {
    #                         "I": 22
    #                     },
    #                     "id": {
    #                         "S": "a88cb45c-0ac1-47b3-865b-a92f05d7612b"
    #                     }
    #                 },
    #                 "StreamViewType": "NEW_IMAGE",
    #                 "SequenceNumber": "111",
    #                 "SizeBytes": 128
    #             },
    #             "awsRegion": "us-west-2",
    #             "eventName": "INSERT",
    #             "eventSourceARN": "event:source:ARN",
    #             "eventSource": "aws:dynamodb"
    #         }
    #     ]
    # }

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
