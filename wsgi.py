# wsgi.py
from flask import Flask
from flask import jsonify
app = Flask(__name__)

PRODUCTS = [
    { 'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' },
    { 'id': 3, 'name': 'Other' }
]

#@app.route('/api/v1/products')
#def products():
#    return jsonify(PRODUCTS)

@app.route('GET /api/v1/products/:<int:post_id>')
    def products(post_id):
        id = post_id
        if id == True:
            return PRODUCTS[id, 'name']
        else:
            return "error 404"
