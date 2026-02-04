# Import Necessary Libraries
from flask import Flask, render_template, request
import pickle

# Creates a Flask application instance named app
app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

# Define the route to handle form submission and make predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get form data (Key:Value)
    try:
        features = {
            'ApplicantIncome': float(request.form['ApplicantIncome']),
            'CoapplicantIncome': float(request.form['CoapplicantIncome']),
            'LoanAmount': float(request.form['LoanAmount']),
            'Loan_Amount_Term': float(request.form['Loan_Amount_Term']),
            'Credit_History': float(request.form['Credit_History']),
            'Dependents_0': 0.0,
            'Dependents_1': 0.0,
            'Dependents_2': 0.0,
            'Dependents_3+': 0.0,
            'Education': float(request.form['Education']),
            'Gender': float(request.form['Gender']),
            'Married': float(request.form['Married']),
            'Property_Area_Rural': float(request.form['Property_Area_Rural']),
            'Property_Area_Semiurban': float(request.form['Property_Area_Semiurban']),
            'Property_Area_Urban': float(request.form['Property_Area_Urban']),
            'Self_Employed': float(request.form['Self_Employed'])
        }
        
        # Convert feature values to a list in the correct order
        feature_values = [
            features['ApplicantIncome'],
            features['CoapplicantIncome'],
            features['LoanAmount'],
            features['Loan_Amount_Term'],
            features['Credit_History'],
            features['Dependents_0'],
            features['Dependents_1'],
            features['Dependents_2'],
            features['Dependents_3+'],
            features['Education'],
            features['Gender'],
            features['Married'],
            features['Property_Area_Rural'],
            features['Property_Area_Semiurban'],
            features['Property_Area_Urban'],
            features['Self_Employed']
        ]
        
        # Make prediction
        prediction = model.predict([feature_values])[0]
        
        # Map prediction to human-readable output
        result = 'Approved' if prediction == 1 else 'Rejected'
        
    except Exception as e:
        result = 'Rejected'
    
    # Render the result template with prediction result
    return render_template('result.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
