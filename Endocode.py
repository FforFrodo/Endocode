from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/helloworld', methods=['GET', 'POST'])
def helloworld():
    #return "Hello Stranger"

#@app.route('/', methods=['GET'])
    if (request.method == 'GET'):
        name = request.args.get('name', type = str)
        return name
    #else:
        #return "Hello Stranger"
    
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