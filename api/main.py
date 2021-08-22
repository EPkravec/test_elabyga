#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from api.base_product import goods

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
client = app.test_client()


def _total_item_quantity():
    number_of_goods_count = 0
    number_of_goods_kilogram = 0
    number_of_goods_liter = 0
    for item in goods:
        if item['unit'] == 'штук':
            number_of_goods_count += item['item_quantity']
        if item['unit'] == 'литров':
            number_of_goods_liter += item['item_quantity']
        if item['unit'] == 'килограмм':
            number_of_goods_kilogram += item['item_quantity']
    total_item_quantity = {'message': 'На складе общее число различных товаров в: %sкг. %sшт. %sл.' % (
        number_of_goods_kilogram, number_of_goods_count, number_of_goods_liter)}
    return total_item_quantity


def _item_and_total_price():
    list_item = []
    item_total = {}
    item_product_name = {}
    item_product_price = {}

    for items in goods:
        for k, v in items.items():
            if k == 'product_name':
                item_product_name['product_name'] = v
            if k == 'price':
                item_product_price['price'] = v
            if k == 'item_quantity':
                item_product_price['item_quantity'] = v
        item_total['price'] = item_product_price['price'] * item_product_price['item_quantity']
        item_total['product_name'] = item_product_name['product_name']
        add_item = item_total.copy()
        list_item.append(add_item)
    return list_item


@app.route('/total-cost', methods=['GET'])
def get_total_price():
    return jsonify(_item_and_total_price())


@app.route('/resources', methods=['GET'])
def get_list():
    return jsonify(goods, _total_item_quantity())


@app.route('/resources', methods=['POST'])
def update_list():
    new_position = request.json
    goods.append(new_position)
    return jsonify(goods)


@app.route('/resources/<int:goods_id>', methods=['PUT'])
def update_goods(goods_id):
    item = next((x for x in goods if x['id'] == goods_id), None)
    params = request.json
    print(params)
    if not item:
        return {'message': 'No goods with this id'}, 400
    item.update(params)
    return item


@app.route('/resources/<int:goods_id>', methods=['DELETE'])
def delete_goods(goods_id):
    idx, _ = next((x for x in enumerate(goods) if x[1]['id'] == goods_id), (None, None))
    params = request.json
    goods.pop(idx)
    return 'delete product accept', 204


if __name__ == '__main__':
    app.run()
