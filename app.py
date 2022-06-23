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

@app.route('/predict',methods=['POST'])
def predict():
    location = request.form.get('location')
    bhk = float(request.form.get('bhk'))
    bath = float(request.form.get('bath'))
    sqft = request.form.get('total_sqft')

    print( location, bhk, bath ,sqft)
    
    input = pd.DataFrame([[location, sqft, bath, bhk]], columns = ['location', 'total_sqft', 'bath' ,'bhk'])
    prediction = pipe.predict(input)[0] * 1e5
    return str(np.round(prediction,2))
    
    
if __name__ == "__main__":
    app.run(debug=True)