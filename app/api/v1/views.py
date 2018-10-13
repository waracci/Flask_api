from flask_restful import Resource, Api, reqparse
from flask import request, make_response, jsonify
from datetime import datetime

carts = []

parser = reqparse.RequestParser()
parser.add_argument('item1')
parser.add_argument('item2')
parser.add_argument('cart_price')

class Carts(Resource):
    def get(self, cart_id=None):
        """Get all carts and if provided with an id gets a single cart"""
        if cart_id is None:
            if len(carts) == 0:
                return make_response(jsonify({
                'message': 'The cart is empty'
                }), 200)
            return make_response(jsonify({
                'status': 'ok',
                'message': 'success',
                'cart': carts
            }), 200)
        cart_item = [cart for cart in carts if int(cart['id']) == int(cart_id)]
        if cart_item:
            return make_response(jsonify({
                'status': 'ok',
                'message': 'success',
                'cart': cart_item
            }), 200)
        return make_response(jsonify({
            'status': 'failed',
            'message': 'not found'
        }), 404)
        
    def post(self):
        """Post cart details"""
        args = parser.parse_args()
        item1 = args['item1']
        item2 = args['item2']
        cart_price = args['cart_price']
        id = len(carts) + 1
        payload = {
            'id': id,
            'description': {
                'item1': item1,
                'item2': item2
            },
            'cart_price': cart_price,
            'date_created': datetime.now(),
            'date_modified': datetime.now()
        }
        carts.append(payload)
        return make_response(jsonify({
            'status': 'ok',
            'message': 'cart success',
            'cart': payload
        }), 201)

    def put(self, cart_id):
        """Edit cart details"""
        args = parser.parse_args()
        item1 = args['item1']
        item2 = args['item2']
        cart_price = args['cart_price']

        cart_item = [cart for cart in carts if int(cart['id']) == int(cart_id)]
        if cart_item:
            if item1:
                cart_item[0]['description']['item1'] = item1
            if item2:
                cart_item[0]['description']['item2'] = item2
            if cart_price:
                cart_item[0]['cart_price'] = cart_price
            cart_item[0]['date_modified'] = datetime.now()
            return make_response(jsonify({
                'status': 'ok',
                'message': 'successfully updated',
                'cart': cart_item 
            }), 200)
        return make_response(jsonify({
            'status': 'failed',
            'message': 'not found'
        }), 404)
     
    def delete(self, cart_id):
        """Delete a cart"""
        cart_item = [cart for cart in carts if int(cart['id']) == int(cart_id)]
        if cart_item:
            carts.remove(cart_item[0])
            return make_response(jsonify({
                'status': 'ok',
                'message': 'cart deleted',
                'cart': cart_item
            }), 200)
        return make_response(jsonify({
            'status': 'failed',
            'message': 'not found'
        }), 404)