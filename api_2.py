import matlab.engine

from flask import Flask, jsonify
from flask import make_response
from flask import request
from flask_restful import Resource, Api, reqparse

import sys
import random

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
api = Api(app)
from flask import abort


#################################################################################
class Forecast(Resource):
    def get(self):
        return {'UNB Forecast': {'LSTM': '/lstm'}}
class Forecast_lstm(Resource):
    

    def post(self):
        if not request.json:
            abort(400)



        input_python = []
        for i in range(79):
            input_python.append([request.json[str(i)]])

        print(input_python, file=sys.stderr)
        input_matlab = matlab.double(input_python)


        eng = matlab.engine.start_matlab()
        output = eng.netLSTMblf_predict(input_matlab)
        eng.quit()

        output_dict = {}

        for i in range(0, 24):
            output_dict[str(i) + ":00"] = output[i][0]

        return {'task': output_dict}, 201

api.add_resource(Forecast_lstm, '/lstm')
api.add_resource(Forecast, '/UNB_algorithms')


#################################################################################

app.run(port=5000, debug=True)
