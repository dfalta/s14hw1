from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load ML models
model_rf = joblib.load('./models/randomforest_regr.pkl')
model_tree = joblib.load('./models/tree_regr.pkl')

# Creat dictionary of model names
model_names = {"model_rf": "Random Forest Regressor", "model_tree": "Decision Tree Regressor"}

@app.route('/')
def index():
	# Set default feature vector = ['BEDS', 'BATHS', 'SQFT', 'AGE', 'LOTSIZE', 'GARAGE']
	X = [[4, 2.5, 3005, 15, 17903.0, 1]]

	# Make prediction.
	prediction = model_rf.predict(X)[0]
	prediction = round(prediction)
	prediction = f'{prediction:,}'

	# Return template.
	return render_template('index.html', price=prediction, X=X[0], model_names=model_names)
	
		
@app.route('/_predict', methods=['POST'])
def getPrediction():
	# Get features from form.
	data = request.form
	X = [[float(data["inpt_beds"]), float(data["inpt_baths"]), float(data["inpt_sqft"]), float(data["inpt_age"]), float(data["inpt_lotsize"]), float(data["inpt_garages"])]]
	
	# Make prediction depending on selected model.
	if data["inpt_model"] == "model_rf":
		prediction = model_rf.predict(X)[0]
	elif data["inpt_model"] == "model_tree":
		prediction = model_tree.predict(X)[0]
	else:
		print("SOMETHING TERRIBLE HAPPENED WHEN SELECTING MODEL")
	prediction = round(prediction)
	prediction = f'{prediction:,}'
	
	# Return prediction.
	return prediction