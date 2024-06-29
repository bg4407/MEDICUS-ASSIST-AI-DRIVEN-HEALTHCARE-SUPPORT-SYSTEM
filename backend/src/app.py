from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Shanchow1234!",
            database="medicus_assist"
        )
        return conn
    except mysql.connector.Error as err:
        print("Database connection failed:", err)
        return None

@app.route('/register', methods=['POST'])
def register():
    try:
        print("Request received with data:", request.json)
        username = request.json.get('username')
        plain_password = request.json.get('password')

        if not plain_password or len(plain_password) < 8 or not re.search(r"[0-9]", plain_password) or not re.search(r"[!@#$%^&*(),.?\":{}|<>]", plain_password):
            return jsonify({'error': 'Password must be at least 8 characters long and include a number and a symbol.'}), 400

        conn = get_db_connection()
        if conn is None:
            return jsonify({'error': 'Database connection error'}), 500
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        if cursor.fetchone() is not None:
            conn.close()
            return jsonify({'error': 'Username already taken'}), 409

        hashed_password = bcrypt.generate_password_hash(plain_password).decode('utf-8')
        cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, hashed_password))
        conn.commit()
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()
        conn.close()
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        print("An error occurred:", e)
        return jsonify({'error': 'Server error'}), 500

@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.json['username']
        password = request.json['password']
        conn = get_db_connection()
        if conn is None:
            return jsonify({'error': 'Database connection error'}), 500
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()
        conn.close()

        if user and bcrypt.check_password_hash(user['password'], password):
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'error': 'Invalid username or password'}), 401
    except Exception as e:
        print("An error occurred during login:", e)
        return jsonify({'error': 'Server error during login'}), 500

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    print(f"Request received: {req}")

    # Ensure we have the expected structure
    if 'queryResult' not in req:
        print("Error: 'queryResult' not in request")
        return jsonify({"fulfillmentMessages": [{"text": {"text": ["Error: 'queryResult' not in request"]}}]}), 400

    intent = req['queryResult'].get('intent', {}).get('displayName', '')
    print(f"Intent: {intent}")
    response_text = ""

    if intent == "Default Welcome Intent":
        response_text = "Hi! I am your medical assistant. How can I help you today?"
    elif intent == "Appointment Scheduling":
        response_text = "Sure, I can help with that. What type of doctor do you need to schedule an appointment with and when?"
    elif intent == "Medical Advice":
        symptoms = req['queryResult']['queryText']
        response_text = get_medical_advice(symptoms)
    elif intent == "Health Monitoring":
        response_text = "I can help monitor your health. What specific health metrics would you like to track?"
    elif intent == "Medication Reminders":
        response_text = "I can set up medication reminders for you. Please provide the medication name and the schedule."
    else:
        response_text = "Sorry, I didn't understand that."

    print(f"Response Text: {response_text}")

    res = {
        "fulfillmentMessages": [
            {
                "text": {
                    "text": [response_text]
                }
            }
        ]
    }

    print(f"Response Payload: {res}")

    return jsonify(res)

def get_medical_advice(symptoms):
    advice = {
        "headache": "It sounds like you have a headache. You might try taking some rest and drinking plenty of water. If it persists, consider taking a pain reliever like ibuprofen or acetaminophen.",
        "fever": "For a fever, it's important to stay hydrated and rest. Over-the-counter medications like acetaminophen or ibuprofen can help reduce the fever.",
        "cough": "If you have a cough, staying hydrated is important. Warm drinks like tea with honey can soothe your throat. If the cough persists, you might consider seeing a doctor.",
        "cold": "Common cold symptoms can be managed with rest, fluids, and over-the-counter medications like decongestants and pain relievers.",
        "stomach ache": "For a stomach ache, try to rest and avoid eating heavy meals. Drinking clear fluids and eating light, bland foods like crackers or toast might help.",
        "allergy": "If you're experiencing allergies, over-the-counter antihistamines can help. Avoiding the allergen and keeping your living space clean can also reduce symptoms.",
        "injury": "For minor injuries, applying ice and keeping the affected area elevated can help reduce swelling. If it's severe, please seek medical attention.",
        "stress": "Managing stress involves regular exercise, healthy eating, and adequate sleep. Techniques like deep breathing, meditation, and talking to someone can also be beneficial.",
        "anxiety": "For anxiety, practices like deep breathing, meditation, and talking to a therapist can help. Regular physical activity and avoiding caffeine can also be beneficial.",
        "fatigue": "If you're feeling fatigued, make sure you're getting enough sleep and eating a balanced diet. Regular physical activity can also improve energy levels.",
        "back pain": "For back pain, try to rest and avoid heavy lifting. Applying ice or heat, as well as taking over-the-counter pain relievers, can help. If pain persists, consult a doctor.",
        "nausea": "For nausea, try sipping clear fluids and eating bland foods like crackers or toast. Ginger tea or peppermint can also help soothe your stomach.",
        "insomnia": "If you're having trouble sleeping, establish a regular sleep schedule, create a restful environment, and avoid caffeine and electronics before bed.",
        "diarrhea": "For diarrhea, stay hydrated with clear fluids and consider over-the-counter medications like loperamide. Avoid dairy and high-fiber foods until you feel better.",
        "constipation": "For constipation, increase your fiber intake with fruits, vegetables, and whole grains. Drinking plenty of water and staying active can also help.",
        "sore throat": "For a sore throat, drink warm liquids like tea with honey, and use throat lozenges. Gargling with salt water can also provide relief.",
        "earache": "For an earache, applying a warm compress and taking over-the-counter pain relievers can help. If pain persists, see a doctor.",
        "rash": "If you have a rash, avoid scratching and try applying a gentle moisturizer or hydrocortisone cream. If it gets worse, consult a doctor.",
        "burn": "For minor burns, cool the area with running water and apply aloe vera or a burn ointment. Cover it with a sterile bandage and avoid popping any blisters.",
        "dehydration": "For dehydration, drink plenty of water and consider oral rehydration solutions. Avoid caffeine and alcohol, which can worsen dehydration.",
        "dizziness": "If you feel dizzy, sit or lie down and avoid sudden movements. Drinking water and eating something can also help if dizziness is due to low blood sugar."
    }

    for symptom in advice:
        if symptom in symptoms:
            return advice[symptom]
    
    return "I'm sorry, I didn't understand that. Can you please describe your symptoms or issue in more detail?"

if __name__ == '__main__':
    app.run(debug=True, port=8080)
