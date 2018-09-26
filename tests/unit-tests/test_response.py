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

        new_headers_expectation = Response.SECURITY_HEADERS

        response = Response(original_response)

        assert type(Response(original_response)) == Response
        assert response.with_security_headers() == {'body': '{"foo": "bar"}',
                                                    'headers': new_headers_expectation,
                                                    'statusCode': 200}

    def test_with_security_headers_and_preexisting(self):
        original_headers = {
            'foo': 'bar'
        }

        original_response = {
            "statusCode": 200,
            "body": json.dumps({'foo': 'bar'}),
            # We're adding to make sure it's not overwritten
            'headers': original_headers
        }

        new_headers_expectation = {}
        new_headers_expectation.update(original_headers)
        new_headers_expectation.update(Response.SECURITY_HEADERS)

        response = Response(original_response)

        assert type(Response(original_response)) == Response
        assert response.with_security_headers() == {'body': '{"foo": "bar"}',
                                                    'headers': new_headers_expectation,
                                                    'statusCode': 200}
