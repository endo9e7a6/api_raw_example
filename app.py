from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


def check_posted_data(posted_data, function_name):
    if function_name in ['add', 'substract', 'multiply', 'divide']:
        if "x" not in posted_data or "y" not in posted_data:
            return 301
        if type(posted_data["x"]) not in [int, float] or type(posted_data["y"]) not in [int, float]:
            return 302
    if function_name in ['divide']:
        if posted_data["y"] == 0:
            return 303
    return 200


class Add(Resource):
    def post(self):
        posted_data = request.get_json()

        status_code = check_posted_data(posted_data, 'add')
        if status_code != 200:
            return jsonify({
                "Message": "An error has occurred",
                "Status Code": status_code
            })

        x = posted_data["x"]
        y = posted_data["y"]

        return jsonify({
            "Message": x+y,
            "Status Code": 200
        })


class Substract(Resource):
    def post(self):
        posted_data = request.get_json()

        status_code = check_posted_data(posted_data, 'substract')
        if status_code != 200:
            return jsonify({
                "Message": "An error has occurred",
                "Status Code": status_code
            })

        x = posted_data["x"]
        y = posted_data["y"]

        return jsonify({
            "Message": x - y,
            "Status Code": 200
        })


class Multiply(Resource):
    def post(self):
        posted_data = request.get_json()

        status_code = check_posted_data(posted_data, 'multiply')
        if status_code != 200:
            return jsonify({
                "Message": "An error has occurred",
                "Status Code": status_code
            })

        x = posted_data["x"]
        y = posted_data["y"]

        return jsonify({
            "Message": x * y,
            "Status Code": 200
        })


class Divide(Resource):
    def post(self):
        posted_data = request.get_json()

        status_code = check_posted_data(posted_data, 'divide')
        if status_code != 200:
            return jsonify({
                "Message": "An error has occurred",
                "Status Code": status_code
            })

        x = posted_data["x"]
        y = posted_data["y"]

        return jsonify({
            "Message": x / y,
            "Status Code": 200
        })


api.add_resource(Add, "/add")
api.add_resource(Substract, "/substract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000", debug=True)
