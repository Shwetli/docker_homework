from flask import Flask, request, jsonify
import psycopg2
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_db_connection():
    return psycopg2.connect(
        dbname=os.environ['POSTGRES_DB'],
        user=os.environ['POSTGRES_USER'],
        password=os.environ['POSTGRES_PASSWORD'],
        host='db'
    )

@app.route('/api/messages', methods=['GET', 'POST'])
def messages():
    conn = get_db_connection()
    cur = conn.cursor()
    if request.method == 'POST':
        data = request.get_json()
        cur.execute("INSERT INTO messages (content) VALUES (%s)", (data['content'],))
        conn.commit()
    cur.execute("SELECT * FROM messages ORDER BY id DESC")
    results = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(results)