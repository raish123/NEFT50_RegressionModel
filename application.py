from flask import Flask, render_template, request
import pickle
import numpy as np
from src.NEFT50.Pipelines.prediction import PredictionPipleine
import os,sys

app = Flask(__name__)

@app.route('/train',methods=['GET'])
def training():
    os.system(command="python main.py")
    return "Training Successfull"



@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Collect data from form
        open_val = float(request.form['open'])
        high_val = float(request.form['high'])
        low_val = float(request.form['low'])
        close_val = float(request.form['close'])
        volume_val = float(request.form['volume'])

        # Convert into array for model input
        features = np.array([[open_val, high_val, low_val, close_val, volume_val]])

        obj = PredictionPipleine()
        prediction = obj.predict(features)


        return render_template('home.html', prediction=str(prediction))

    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)