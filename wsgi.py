# wsgi.py
from flask import Flask, abort, request
from flask import jsonify
app = Flask(__name__)

PRODUCTS = [
    { 'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' },
    { 'id': 3, 'name': 'Other' }
]

'''Affiche le dict products'''
@app.route('/api/v1/products')
def products():
    return jsonify(PRODUCTS)

'''GET'''
@app.route('/api/v1/products/<int:post_id>', methods=['GET'])
def products_read(post_id):
    for product in PRODUCTS:
        if post_id == product['id']:
            return jsonify(product)
    abort (404)

'''DELETE'''
@app.route('/api/v1/products/<int:post_id>', methods=['DELETE'])
def products_delete(post_id):
        for product in PRODUCTS:
            if post_id == product['id']:
                del product['id']
                abort(204)
