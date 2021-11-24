from flask import Flask, request
from flask.json import jsonify
import sqlite3
from datetime import datetime as dt


app = Flask(__name__)


def store(query):
    conn = sqlite3.connect('database.db')
    conn.execute(query)
    conn.commit()
    conn.close()


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/storeIp', methods=['POST', 'GET'])
def storeIp():
    if request.method == 'POST':
        ip = request.args.get('ip')
        print(ip)
        store(
            f'INSERT INTO ip(timestamp, ip) VALUES("{dt.now().strftime("%Y-%m-%D %I:%m:%S %p")}","{ip}")')

        return jsonify(status='storedIp')
    else:
        print('get method')
        return 'get method'


if __name__ == '__main__':
    app.run(debug=True)
