from flask import Blueprint, request, jsonify,render_template
import joblib

main = Blueprint('main', __name__)

model = joblib.load('models/allergen_predictor.pkl')
label_encoders = joblib.load('models/label_encoders.pkl')
@main.route('/')
def index():
    return render_template('index.html')

@main.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = []

    for column in label_encoders:
        le = label_encoders[column]
        encoded_value = le.transform([data[column]])[0]
        features.append(encoded_value)

    prediction = model.predict([features])[0]
    contains_allergen = 'Contains' if prediction == 1 else 'Does not contain'

    return jsonify({'prediction': contains_allergen})
