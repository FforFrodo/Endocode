from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/helloworld', methods=['GET', 'POST'])
def helloworld():

    if (request.method == 'GET'):
        name = request.args.get('name', type = str)
        for i in range(len(name)-1)[::-1]:
            if name[i].isupper() and name[i+1].islower():
                name = name[:i]+' '+name[i:]
            if name[i].isupper() and name[i-1].islower():
                name = name[:i]+' '+name[i:]
        b =  name.split()
        a = ' '
        NewName = a.join(b)
        return 'Hello ' + (NewName)
    else:
        return 'Hello Stranger'
    
    #---This is from a tutorial
    #if (request.method == 'POST'):
        #some_json = request.get_json()
        #return jsonify({'You sent': some_json}), 201
    #else:
        #return jsonify({"about":"Hello Stranger"})


@app.route('/multi/<int:num>', methods=['GET'])
def get_multiply10(num):
    return jsonify({'result':num*10})

if __name__ == '__main__':
        app.run(debug=True)