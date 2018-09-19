import json
import logging
import os
import time
import uuid

import boto3
dynamodb = boto3.resource('dynamodb')

from scans import Target


def create(event, context):
    data = json.loads(event['body'])

    target = Target(data.get['target'])
    if target.valid() == False:
        logging.error("Target Validation Failed")
        raise Exception("No target or invalid target specified.")
        return

    if 'port' not in data:
        logging.error("Validation Failed")
        raise Exception("No 'port' was specified.")
        return

    timestamp = int(time.time() * 1000)

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'id': str(uuid.uuid1()),
        'target': data['target'],
        'port': data['port'],
        'createdAt': timestamp,
        'updatedAt': timestamp,
    }

    # write the todo to the database
    table.put_item(Item=item)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response
