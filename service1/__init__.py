#Endocode Technical Challenge
#Kevin Donnelly

#Imports
from flask import Flask, request, json
from decouple import config
import logging
import subprocess
import re
import os
import sys

#New Log is generated if not found (Listening port, date, HTTP status, requests)
logging.basicConfig(filename='Structured.log', level=logging.DEBUG)

#Create an instance of Flask
app = Flask(__name__)

# /helloworld returns 'Hello Stranger' 
# http://0.0.0.0:8080/helloworld

# /helloworld?name=AlfredENeumann (any filtered value) returns 'Hello Alfred E Neumann'
# http://0.0.0.0:8080/helloworld?name=AlfredENeumann
@app.route('/helloworld', methods=['GET'])
def hello_world():
    if request.args:
        query_name = request.args.get("name", "")
        user_name = (re.sub(r"(?<=\w)([A-Z])", r" \1", query_name)).title()
        return f"Hello {user_name}"
    else:
        return f'Hello Stranger'

# Returns a JSON with {Project name : Commit hash}
# http://0.0.0.0:8080/versionz
@app.route('/versionz')
def get_git_revision_hash():
    try:
        latest_commit_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD'])
        latest_commit_hash = latest_commit_hash.rstrip()
    # If not copying .git folder into docker container
    except Exception as e:
        print(e)

    project_name = config('COMPOSE_PROJECT_NAME') #from Enviornment variable set in .env
    values = {f"{project_name}": f"{latest_commit_hash.decode('utf-8')}"}
    return json.dumps(values)

# python run.py