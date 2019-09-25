# tests/test_views.py
from flask_testing import TestCase
from wsgi import app

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_read_products(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 2) # 2 is not a mistake here.

    def test_read_product_success(self):
        response = self.client.get("/api/v1/products/1")
        product = response.json
        self.assertEqual(product['id'], 1)

    def test_read_product_fail(self):
        response = self.client.get("/api/v1/products/9")
        self.assertEqual(response.status_code, 404)

    def test_delete_product_success(self):
        first_response = self.client.get("/api/v1/products")
        first_products = first_response.json
        self.assertEqual(len(first_products), 3)

        response = self.client.get("/api/v1/products/1")
        self.assertEqual(response.status_code, 204)

        second_response = self.client.get("/api/v1/products")
        second_products = second_response.json
        self.assertEqual(len(second_products), 2)

    def test_delete_product_fail(self):
        response = self.client.get("/api/v1/products/9")
        self.assertEqual(response.status_code, 404)
