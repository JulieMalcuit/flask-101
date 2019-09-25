# tests/test_views.py
from flask_testing import TestCase
from wsgi import app

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

#    def test_products_json(self):
#        response = self.client.get("/api/v1/products")
#        products = response.json
#        self.assertIsInstance(products, list)
#        self.assertGreater(len(products), 2) # 2 is not a mistake here.

    def test_products_r(self):
        response = self.client.get('GET /api/v1/products/:1')
        products = response.json
        self.assertEquals ((products[4]), "Skello")
