import os
import json
import boto3
import logging
import time

logger = logging.getLogger()
logger.setLevel(logging.INFO)
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])


def worker(event, context):
    # logger.info('## ENVIRONMENT VARIABLES')
    # logger.info(os.environ)
    # logger.info('## EVENT')
    # logger.info(event)

    for record in event["Records"]:
        if not record["eventName"] == "INSERT":
            continue

        image = record["dynamodb"]["NewImage"]
        scan_id = image["id"]["S"]
        target = image["target"]["S"]
        port = int(image["port"]["N"])

        # TODO: Add real scan logic here to populate scan var, probably via a scan-engine
        #  class implemented in Python instead of Ruby
        #  https://github.com/mozilla/ssh_scan/blob/master/lib/ssh_scan/scan_engine.rb
        # In the mean time, we'll manually curate for the sake of example/testing
        scan = {
            'target': target,
            'port': port,
            'foo': 'bar'
        }
        time.sleep(5)

        table.update_item(
            Key={
                'id': scan_id
            },
            UpdateExpression='SET #scanresult = :val1',
            ExpressionAttributeValues={
                ':val1': scan,
            },
            ExpressionAttributeNames={
                "#scanresult": "scan",
            }
        )

        status = "COMPLETED"
        table.update_item(
            Key={
                'id': scan_id
            },
            UpdateExpression='SET #statusresult = :val1',
            ExpressionAttributeValues={
                ':val1': status,
            },
            ExpressionAttributeNames={
                "#statusresult": "status",
            }
        )
