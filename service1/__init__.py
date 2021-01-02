#Endocode Technical Challenge
#Kevin Donnelly

#Imports
from flask import Flask, request, json
import logging
import subprocess
import re
import os
import sys

#Log (Listening port, date, HTTP status, requests) to log file
logging.basicConfig(filename='Structured.log', level=logging.DEBUG)

#Create an instance of Flask
app = Flask(__name__)

# /helloworld returns 'Hello Stranger' 
# http://0.0.0.0:8080/helloworld

# /helloworld?name=AlfredENeumann (any filtered value) returns 'Hello Alfred E Neumann'
# http://0.0.0.0:8080/helloworld?name=
@app.route('/helloworld', methods=['GET'])
def hello_world():
    if request.args:
        query_name = request.args.get("name", "")
        user_name = (re.sub(r"(?<=\w)([A-Z])", r" \1", query_name)).title()
        return f"Hello {user_name}"
    else:
        return f'Hello Stranger'

# Returns a JSON with Githash and name of the project
# http://0.0.0.0:8080/versionz
@app.route('/versionz')
def get_git_revision_hash():
    try:
        latest_commit_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD'])
        
    # If not copying .git folder into docker container
    except Exception as e:
        print(e)
    # Returns Project name from git repo name and latest git commit hash
    repo_path = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'])
    project_name = os.path.basename(repo_path)

    values = {f"{project_name}": f"{latest_commit_hash}"}
    return json.dumps(values)
