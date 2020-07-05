from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load ML model 
model = joblib.load('./models/randomforest_regr.pkl')

@app.route('/')
def index():
	# Set default feature vector = ['BEDS', 'BATHS', 'SQFT', 'AGE', 'LOTSIZE', 'GARAGE']
	X = [[4, 2.5, 3005, 15, 17903.0, 1]]

	# Make prediction.
	prediction = model.predict(X)[0]
	prediction = round(prediction)
	prediction = f'{prediction:,}'

	# Return template.
	return render_template('index.html', price=prediction, X=X[0])
	
		
@app.route('/_predict', methods=['POST'])
def getPrediction():
	# Get features from form.
	data = request.form
	X = [[float(data["inpt_beds"]), float(data["inpt_baths"]), float(data["inpt_sqft"]), float(data["inpt_age"]), float(data["inpt_lotsize"]), float(data["inpt_garages"])]]
	
	# Make prediction.
	prediction = model.predict(X)[0]
	prediction = round(prediction)
	prediction = f'{prediction:,}'
	
	# Return prediction.
	return prediction