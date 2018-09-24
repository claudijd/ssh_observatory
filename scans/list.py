import json
import os

from scans import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')
from scans import Response


def list(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    result = table.scan()

    return Response({
        "statusCode": 200,
        "body": json.dumps(result['Items'], cls=decimalencoder.DecimalEncoder)
    }).with_security_headers()
