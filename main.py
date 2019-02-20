from flask import Flask, render_template, jsonify
from flask_restful import Resource, Api, request


app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return render_template('body.html')

class test(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        print(json_data)
        return json_data
        # return jsonify(newdata=newdata)

api.add_resource(test, '/v1/test')
api.add_resource(addtime, '/v1/post')