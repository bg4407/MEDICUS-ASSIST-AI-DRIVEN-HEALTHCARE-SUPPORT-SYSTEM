from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app)

# Database connection function
def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="mydatabase"
    )
    return conn

@app.route('/')
def home():
    return jsonify({'message': 'Healthcare Chatbot API'})

@app.route('/info', methods=['GET'])
def get_info():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT info FROM information")  # Example SQL query
    info = cursor.fetchone()
    conn.close()
    return jsonify({'info': info})

@app.route('/appointment', methods=['POST'])
def schedule_appointment():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    # Example SQL command to insert appointment
    cursor.execute("INSERT INTO appointments (details) VALUES (%s)", (data['details'],))
    conn.commit()
    conn.close()
    return jsonify({'status': 'Appointment scheduled', 'details': data})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)
