import time
import mysql.connector
from flask import Flask, jsonify
import os

app = Flask(__name__)

def wait_for_mysql():
    for i in range(10):
        try:
            conn = mysql.connector.connect(
                host=os.environ.get("MYSQL_HOST"),
                user=os.environ.get("MYSQL_USER"),
                password=os.environ.get("MYSQL_PASSWORD"),
                database=os.environ.get("MYSQL_DATABASE")
            )
            print("✅ MySQL підключено успішно!")
            return conn
        except mysql.connector.Error as e:
            print(f"❌ Спроба {i+1}: БД ще не готова. Повтор через 3 секунди...")
            time.sleep(3)
    raise Exception("🚫 Не вдалося зʼєднатись з MySQL після 10 спроб.")

# 🔁 Чекаємо підключення
db = wait_for_mysql()

@app.route("/users")
def get_users():
    try:
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        return jsonify(users)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    @app.route("/health")
    def health():
        return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
