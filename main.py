from flask import Flask, render_template, jsonify
from flask_restful import Resource, Api, request


app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return render_template('body.html')

@app.route('/api/test')
def api_test():
    try:
        return jsonify({'state': 'Succes!'})
    except:
        return jsonify({'state': 'Failed!'})

class test(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        print(json_data)
        print(request.headers.get('Authorization'))
        return json_data
        # return jsonify(newdata=newdata)

api.add_resource(test, '/v1/test')

def main():
    app.run(debug=True, host='0.0.0.0', port=5000)

main()