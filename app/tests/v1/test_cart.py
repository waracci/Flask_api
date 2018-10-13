import unittest
from flask import json
from app.apps import create_app

class TestOrder(unittest.TestCase):
    """Tests for Cart in flask api"""

    def setUp(self):
        """Set up variables for use during testing"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.cart_data = {'item1': 'Short','item2': 'Vest','cart_price': 2000}

    def test_post_cart(self):
        """Test that user can post a single cart"""

        result = self.client().post(
            '/api/v1/cart', data=self.cart_data)
        res = json.loads(result.data.decode())
        self.assertEqual((res['message']), 'cart success')
        self.assertEqual(result.status_code, 201)

    def test_get_order(self):
        """Test that a user can get all carts"""

        cart_posted = self.client().post(
            '/api/v1/cart', data=self.cart_data)
        cart_data = json.loads(cart_posted.data.decode())
        self.assertEqual(cart_data['message'], 'cart success')
        self.assertEqual(cart_posted.status_code, 201)

        response_data = self.client().get(
            '/api/v1/cart')
        self.assertEqual(response_data.status_code, 200)
        self.assertIn('Short', str(response_data.data))

    def test_app_can_get_cart_by_id(self):
        """Test that the app can get a single cart by id"""

        single_cart_posted = self.client().post(
            '/api/v1/cart', data=self.cart_data)
        self.assertEqual(single_cart_posted.status_code, 201)
        posted_cart_id = json.loads(single_cart_posted.data.decode())

        check_for_posted_cart_data = self.client().get(
            '/api/v1/cart/{}'.format(posted_cart_id['cart']['id']))
        self.assertEqual(check_for_posted_cart_data.status_code, 200)
        self.assertIn('Short', str(check_for_posted_cart_data.data))

    def test_app_can_edit_cart_details(self):
        """Test that app can edit cart details successfully"""

        cart_posted = self.client().post(
            '/api/v1/cart', data=self.cart_data)
        self.assertEqual(cart_posted.status_code, 201)
        result = json.loads(cart_posted.data.decode())

        edit_request = self.client().put(
            '/api/v1/cart/{}'.format(result['cart']['id']),
            data={"item1": "siagi", "item2": "mkate", "cart_price": 650})
        self.assertEqual(edit_request.status_code, 200)

        edited_cart = self.client().get(
            '/api/v1/cart/{}'.format(result['cart']['id']))
        response = json.loads(edited_cart.data.decode())
        self.assertEqual(edited_cart.status_code, 200)
        self.assertEqual('siagi', str(response['cart'][0]['description']['item1']))
        self.assertEqual('mkate', str(response['cart'][0]['description']['item2']))
        self.assertEqual(650, int(response['cart'][0]['cart_price']))

    def test_app_can_delete_single_cart(self):
        """Test that app can delete a cart entry successfully"""
        
        cart_posted = self.client().post(
            '/api/v1/cart', data=self.cart_data)
        self.assertEqual(cart_posted.status_code, 201)
        result = json.loads(cart_posted.data.decode())

        cart_delete = self.client().delete(
            '/api/v1/cart/{}'.format(result['cart']['id']))
        self.assertEqual(cart_delete.status_code, 200)

        cart_confirm_delete = self.client().get(
            '/api/v1/cart/{}'.format(result['cart']['id']))
        response = json.loads(cart_confirm_delete.data.decode())
        self.assertEqual(cart_confirm_delete.status_code, 404)
        self.assertEqual('not found', response['message'])

    def tearDown(self):
        """Empty the cart data"""
        self.cart_data = {}

if __name__=='__main__':
    unittest.main()