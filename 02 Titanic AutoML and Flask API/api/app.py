from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import autokeras as ak
from tensorflow.keras.models import load_model

loaded_model = load_model("../model_autokeras", custom_objects=ak.CUSTOM_OBJECTS)

app = Flask(__name__)


@app.route('/api/survival', methods=['GET'])
def predict_survival():
    """
    expects array of rows in request body
    :return: array of predicted values, 1 is "Survived"
    """
    records = pd.read_json(request.data)
    predictions = loaded_model.predict(records.astype(np.unicode))
    return jsonify(predictions.T[0].tolist())


if __name__ == '__main__':
    app.run()
