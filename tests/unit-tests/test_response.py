import pytest
import sys
import os
import json

sys.path.append(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '../..'))

from scans import Response


class TestResponse():
    def test_without_security_headers(self):
        original_response = {
            "statusCode": 200,
            "body": json.dumps({'foo': 'bar'})
        }

        response = Response(original_response)

        assert type(Response(original_response)) == Response
        assert response.without_security_headers() == {
            'body': '{"foo": "bar"}', 'statusCode': 200}

    def test_with_security_headers(self):
        original_response = {
            "statusCode": 200,
            "body": json.dumps({'foo': 'bar'})
        }

        response = Response(original_response)

        assert type(Response(original_response)) == Response
        assert response.with_security_headers() == {'body': '{"foo": "bar"}',
                                                    'headers': {'Access-Control-Allow-Methods': 'GET, POST, OPTIONS, HEAD',
                                                                'Access-Control-Allow-Origin': '*',
                                                                'Access-Control-Max-Age': '86400',
                                                                'Cache-control': 'no-store',
                                                                'Content-Security-Policy': "default-src 'none'; frame-ancestors 'none'; script-src 'none'; upgrade-insecure-requests",
                                                                'Pragma': 'no-cache',
                                                                'Referrer-Policy': 'no-referrer',
                                                                'Strict-Transport-Security': 'max-age = 15768000; includeSubDomains',
                                                                'X-Content-Type-Options': 'nosniff',
                                                                'X-Download-Options': 'noopen',
                                                                'X-Frame-Options': 'DENY',
                                                                'X-Permitted-Cross-Domain-Policies': 'none',
                                                                'X-XSS-Protection': '1; mode = block'},
                                                    'statusCode': 200}
