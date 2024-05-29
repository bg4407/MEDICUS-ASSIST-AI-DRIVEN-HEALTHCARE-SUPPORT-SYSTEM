import mysql.connector
from flask_bcrypt import Bcrypt

class UserManager:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.bcrypt = Bcrypt()

    def create_user(self, username, email, password):
        cursor = self.db_connection.cursor()
        hashed_password = self.bcrypt.generate_password_hash(password).decode('utf-8')
        try:
            cursor.execute('INSERT INTO users (username, email, password) VALUES (%s, %s, %s)', (username, email, hashed_password))
            self.db_connection.commit()
            return True
        except mysql.connector.Error as err:
            print("Error: ", err)
            return False
        finally:
            cursor.close()

    def verify_user(self, username, password):
        cursor = self.db_connection.cursor(dictionary=True)
        try:
            cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
            user = cursor.fetchone()
            if user and self.bcrypt.check_password_hash(user['password'], password):
                return True
            return False
        finally:
            cursor.close()
