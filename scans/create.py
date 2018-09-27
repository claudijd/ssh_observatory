import json
import logging
import os
import time
import uuid

import boto3
dynamodb = boto3.resource('dynamodb')

from scans import Target
from scans import Port
from scans import Response


def create(event, context):
    data = json.loads(event['body'])

    if not Target(data.get('target')).valid():
        logging.error("Target Validation Failed of: " +
                      json.dumps(data))
        return Response({
            "statusCode": 200,
            "body": json.dumps({'error': 'target was not valid or missing'})
        }).with_security_headers()

    if not Port(data.get('port')).valid():
        logging.error("Port Validation Failed of: " + json.dumps(data))
        return Response({
            "statusCode": 200,
            "body": json.dumps({'error': 'port was not valid or missing'})
        }).with_security_headers()

    timestamp = int(time.time() * 1000)

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'id': str(uuid.uuid1()),
        'target': data['target'],
        'port': data['port'],
        'scan': None,
        'createdAt': timestamp,
        'updatedAt': timestamp,
    }

    # write the scan to the database
    table.put_item(Item=item)

    return Response({
        "statusCode": 200,
        "body": json.dumps(item)
    }).with_security_headers()
