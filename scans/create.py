import json
import logging
import os
import time
import uuid

import boto3
dynamodb = boto3.resource('dynamodb')

from scans import Target
from scans import Port


def create(event, context):
    data = json.loads(event['body'])

    target = Target(data['target'])
    if target.valid() == False:
        logging.error("Target Validation Failed of: " + json.dumps(data))
        response = {
            "statusCode": 200,
            "body": json.dumps({'error': 'target was not specified or target was not valid'})
        }
        return response

    port = Port(data['port'])
    if port.valid() == False:
        logging.error("Port Validation Failed of: " + json.dumps(data))
        response = {
            "statusCode": 200,
            "body": json.dumps({'error': 'port was not specified or port was not valid'})
        }
        return response

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
