import pytest
from flask import Flask, request, json
import re
from service1 import app

def test_hellostranger():
    response = app.test_client().get("http://0.0.0.0:8080/helloworld")
    assert response.status_code == 200

    #Test endpoint returns 'Hello Stranger'
    assert response.data == b'Hello Stranger'


def test_helloname():
    response = app.test_client().get("http://0.0.0.0:8080/helloworld?name=AlfredENeumann")
    assert response.status_code == 200

    #Test Endpoint filters a string and returns Hello + String
    assert response.data == b'Hello Alfred E Neumann'


def test_versionz():
    response = app.test_client().get("http://0.0.0.0:8080/versionz")
    assert response.status_code == 200

    #Test Endpoint returns Project name 'Endocode'
    json_data = json.loads(response.data)
    assert 'Endocode' in json_data

    #Test commit hash in JSON is SHA1
    pattern = re.compile(r'\b[0-9a-f]{40}\b')
    assert re.match(pattern, json_data['Endocode'])

# pytest test.py

