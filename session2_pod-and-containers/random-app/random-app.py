from flask import Flask, jsonify
import os
import random
import logging
from datetime import datetime

app = Flask(__name__)

logging.basicConfig(filename='/var/log/myapp.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Đọc ENV từ file môi trường
def load_env():
    env_file_path = '/config/app.env'
    if os.path.exists(env_file_path):
        with open(env_file_path) as f:
            for line in f:
                name, value = line.strip().split('=')
                os.environ[name] = value

load_env()

MIN = int(os.getenv('MIN', 1))
MAX = int(os.getenv('MAX', 10))
PORT = int(os.getenv('PORT', 8080))

@app.route('/ready', methods=['GET'])
def ready():
    return jsonify({"status": "ok"}), 200

@app.route('/random', methods=['GET'])
def random_number():
    number = random.randint(MIN, MAX)
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logging.info(f"{current_time} - Generated random number: {number}") 
    return jsonify({"random_number": number})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)