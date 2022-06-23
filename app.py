import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
from flask_cors import cross_origin

app = Flask(__name__)
data = pd.read_csv('Cleaned_data.csv')
pipe = pickle.load(open('RidgeModel.pkl', 'rb'))

@app.route("/")
@cross_origin()
def home():
    locations = sorted(data['location'].unique())
    return render_template('index.html',locations=locations)
    
if __name__ == "__main__":
    app.run(debug=True)
