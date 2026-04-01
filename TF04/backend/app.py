from flask import Flask, jsonify, request
import time
import os
from config import INSTANCE_ID, RESPONSE_DELAY

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'instance_id': INSTANCE_ID}), 200

@app.route('/api/info')
def info():
    time.sleep(RESPONSE_DELAY)
    return jsonify({
        'instance_id': INSTANCE_ID,
        'status': 'ok',
        'timestamp': time.time(),
        'load_factor': globals().get('LOAD_FACTOR', 1.0)
    })

@app.route('/api/products')
def products():
    time.sleep(RESPONSE_DELAY * 0.5)
    products = [
        {'id': 1, 'name': 'Notebook HA', 'price': 4500.00},
        {'id': 2, 'name': 'Smartphone Load Balance', 'price': 2500.00},
        {'id': 3, 'name': 'Tablet Nginx', 'price': 1800.00}
    ]
    return jsonify(products)

@app.route('/api/cart')
def cart():
    time.sleep(RESPONSE_DELAY)
    return jsonify({
        'items': [
            {'name': 'Notebook HA', 'price': 4500.00},
            {'name': 'Smartphone Load Balance', 'price': 2500.00}
        ],
        'total': 7000.00
    })

@app.route('/api/orders', methods=['POST'])
def create_order():
    data = request.json or {}
    time.sleep(RESPONSE_DELAY * 1.5)
    return jsonify({'order_id': f'ORD-{int(time.time())}-{INSTANCE_ID}', 'status': 'created'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

