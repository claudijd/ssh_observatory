import json
import os
import sys
import requests
import pytest

# export a API_URL environment varialble to be something like:
# API_URL="https://something.execute-api.us-west-2.amazonaws.com/dev/"
API_URL = os.environ.get("API_URL", None)


def test_api_url_environtment_variable():
    assert API_URL is not None


if not API_URL.endswith("/"):
    API_URL = API_URL + "/"


def test_api_create():
    response = requests.post('{}scans'.format(API_URL),
                             data=json.dumps(
        {"target": "ssh.mozilla.com", "port": 22}
    )
    )
    entry = response.json()
    assert isinstance(entry, dict)
    assert entry.get('port') == 22
    assert entry.get('target') == "ssh.mozilla.com"
    assert isinstance(entry.get('id'), str)
    assert isinstance(entry.get('createdAt'), int)
    assert isinstance(entry.get('updatedAt'), int)


def test_api_create_missing_target():
    response = requests.post('{}scans'.format(API_URL),
                             data=json.dumps(
        {"port": 22}
    )
    )
    assert response.status_code == 200
    entry = response.json()
    assert isinstance(entry, dict)
    assert entry.get('error') == 'target was not valid or missing'


def test_api_create_missing_port():
    response = requests.post('{}scans'.format(API_URL),
                             data=json.dumps(
        {"target": "ssh.mozilla.com"}
    )
    )
    assert response.status_code == 200
    entry = response.json()
    assert isinstance(entry, dict)
    assert entry.get('error') == 'port was not valid or missing'


def test_api_get():
    response = requests.post('{}scans'.format(API_URL),
                             data=json.dumps(
        {"target": "ssh.mozilla.com", "port": 22}
    )
    )
    assert response.status_code == 200
    entry = response.json()
    assert isinstance(entry, dict)
    assert isinstance(entry.get('id'), str)

    response2 = requests.get('{}scans/{}'.format(API_URL, entry.get('id')))
    entry2 = response2.json()

    assert isinstance(entry2, dict)
    assert isinstance(entry2.get('port'), int)
    assert isinstance(entry2.get('target'), str)
    assert isinstance(entry2.get('id'), str)
    assert isinstance(entry2.get('createdAt'), int)
    assert isinstance(entry2.get('updatedAt'), int)
    assert entry2.get('id') == entry.get('id')
    assert entry2.get('port') == entry.get('port')
    assert entry2.get('target') == entry.get('target')
    assert entry2.get('createdAt') == entry.get('createdAt')
    assert entry2.get('updatedAt') == entry.get('updatedAt')


def test_api_list():
    response = requests.get('{}scans'.format(API_URL))
    assert isinstance(response.json(), list)
    for entry in response.json():
        assert isinstance(entry, dict)
        assert isinstance(entry.get('port'), int)
        assert isinstance(entry.get('target'), str)
        assert isinstance(entry.get('id'), str)
        assert isinstance(entry.get('createdAt'), int)
        assert isinstance(entry.get('updatedAt'), int)
