from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    intent = req.get('queryResult').get('intent').get('displayName')
    parameters = req.get('queryResult').get('parameters')

    if intent == "Headache":
        response = "It sounds like you have a headache. You might try taking some rest and drinking plenty of water. If it persists, consider taking a pain reliever like ibuprofen or acetaminophen."
    elif intent == "Fever":
        response = "For a fever, it's important to stay hydrated and rest. Over-the-counter medications like acetaminophen or ibuprofen can help reduce the fever."
    elif intent == "Schedule Appointment":
        response = "Sure, I can help you with that. Please provide the date, time, and type of doctor you prefer for the appointment."
    elif intent == "Provide Appointment Details":
        date_time = parameters.get('date-time')
        doctor_type = parameters.get('doctor-type')
        response = f"Thank you. I have scheduled your appointment for {date_time} with {doctor_type}."
    else:
        response = "I'm sorry, I didn't understand that. Can you please describe your symptoms or issue in more detail?"

    return jsonify({"fulfillmentText": response})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
