#REST API with Flask for Endocode Technical challenge level 1
#Kevin Donnelly

from flask import Flask, jsonify, request
import subprocess
app = Flask(__name__)


# /helloworld retunrs 'Hello Stranger' 
# http://0.0.0.0:8080/helloworld

#/helloworld?name + <StringString> returns 'Hello <String String>'
# http://0.0.0.0:8080/helloworld?name=
@app.route('/helloworld', methods=['GET', 'POST'])
def helloworld():

    if (request.method == 'GET'):
        name = request.args.get('name', default = None, type = str)

        for i in range(len(name)-1)[::-1]:
            if name[i].isupper() and name[i+1].islower():
                name = name[:i]+' '+name[i:] 
            if name[i].isupper() and name[i-1].islower():
                name = name[:i]+' '+name[i:]
        b =  name.split() #Camel case string is split into a list 
        a = ' ' #blank spaces for .join
        NewName = a.join(b) #joins strings from list into 1 string with spaces
        return 'Hello ' + (NewName) #Success

    else:
        return 'Hello Stranger' #Doesn't work
    
    #---This is from a tutorial
    #if (request.method == 'POST'):
        #some_json = request.get_json()
        #return jsonify({'You sent': some_json}), 201
    #else:
        #return jsonify({"about":"Hello Stranger"})


# Returns a JSON with Githash and name of the project
# http://0.0.0.0:8080/versionz
@app.route('/versionz', methods=['GET'])
def get_git_revision_hash():
    GitHash = subprocess.check_output(['git', 'rev-parse', 'HEAD'])
    return jsonify({'Endocode':GitHash})


#Bonus: multiplication function for testing purposes
# http://0.0.0.0:8080/multi/
@app.route('/multi/<int:num>', methods=['GET'])
def get_multiply10(num):
    return jsonify({'result':num*10})


#Runs on port http://0.0.0.0:8080/
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8080, debug=True)


# http://0.0.0.0:8080/helloworld
# http://0.0.0.0:8080/helloworld?name=  <...>
# http://0.0.0.0:8080/versionz
# http://0.0.0.0:8080/multi/