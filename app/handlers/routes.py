import this
from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np
import os

def configure_routes(app):

    this_dir = os.path.dirname(__file__)
    model_path = os.path.join(this_dir, "model.pkl")
    clf = joblib.load(model_path)

    @app.route('/')
    def hello():
        return "try the predict route it is great!"


    @app.route('/predict')
    def predict():
        #use entries from the query string here but could also use json
        if "G1" not in request.args:
            return "Invalid Inputs Supplied", 400
        if "G2" not in request.args:
            return "Invalid Inputs Supplied", 400
        if "studytime" not in request.args:
            return "Invalid Inputs Supplied", 400
        if "absences" not in request.args:
            return "Invalid Inputs Supplied", 400
        if "freetime" not in request.args:
            return "Invalid Inputs Supplied", 400
        if "failures" not in request.args:
            return "Invalid Inputs Supplied", 400
        g1 = request.args.get('G1', type=int, default=-1)
        g2 = request.args.get('G2', type=int, default=-1)
        studytime = request.args.get('studytime', type=int, default=-1)
        absences = request.args.get('absences', type=int, default=-1)
        freetime = request.args.get('freetime', type=int, default=-1)
        failures = request.args.get('failures', type=int, default=-1)

        if g1 < 0  or g1 > 20:
            return "Out of Range Inputs Supplied", 405
        if g2 < 0  or g2 > 20:
            return "Out of Range Inputs Supplied", 405
        if studytime < 1  or studytime > 4:
            return "Out of Range Inputs Supplied", 405
        if absences < 0  or absences > 93:
            return "Out of Range Inputs Supplied", 405
        if freetime < 1  or freetime > 5:
            return "Out of Range Inputs Supplied", 405
        if failures < 0  or failures > 4:
            return "Out of Range Inputs Supplied", 405

        data = [[g1], [g2], [studytime],[absences], [freetime], [failures]]
        query_df = pd.DataFrame({
            'G1' : pd.Series(g1),
            'G2' : pd.Series(g2),
            'studytime' : pd.Series(studytime),
            'absences': pd.Series(absences),
            'freetime' : pd.Series(freetime),
            'failures': pd.Series(failures)
        })
        query = pd.get_dummies(query_df)
        prediction = clf.predict(query)
        return jsonify({'prediction': np.ndarray.item(prediction)})
