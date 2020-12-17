#REST API with Flask for Endocode technical challenge Level 1
#Kevin Donnelly

from flask import Flask, jsonify, request
import subprocess, re
import json
app = Flask(__name__)


# /helloworld returns 'Hello Stranger' 
# http://0.0.0.0:8080/helloworld

#/helloworld?name=AlfredENeumann (any filtered value) returns 'Hello Alfred E Neumann'
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
    latest_commit_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD'])
    values = {"Endocode.py": f"{latest_commit_hash}"}
    return json.dumps(values)


#Bonus: multiplication function for testing purposes
# http://0.0.0.0:8080/multi/
@app.route('/multi/<int:num>', methods=['GET'])
def get_multiply10(num):
    return jsonify({'result':num*10})


#Run on port http://0.0.0.0:8080/
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8080, debug=True)

#Test URLs
# http://0.0.0.0:8080/helloworld
# http://0.0.0.0:8080/helloworld?name=AlfredENeumann
# http://0.0.0.0:8080/versionz
# http://0.0.0.0:8080/multi/10