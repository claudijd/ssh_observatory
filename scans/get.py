import os
import json

from scans import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')
from scans import Response


def get(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    return Response({
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                           cls=decimalencoder.DecimalEncoder)
    }).with_security_headers()
