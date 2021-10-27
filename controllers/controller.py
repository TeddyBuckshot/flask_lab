from flask import render_template
from app import app
from models.order_list import cars

@app.route('/orders')
def index():
    return render_template('index.html', title='Home Page', group_of_orders = cars)

@app.route('/car_order/<index_of_current_car_selection>')
def car_page(index_of_current_car_selection):
    return render_template('order.html', title='Car Page', single_order = cars[int(index_of_current_car_selection)])

