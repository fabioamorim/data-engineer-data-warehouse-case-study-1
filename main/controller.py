from customer import Customer
from location import Location
from product import Product
from order import Order

import load_data

from csv import DictReader

import time

def execute_etl(source):

    list_orders = []

    #extract
    with open(source, encoding='utf-8') as file:

        data = DictReader(file)

        for row in data:

            order = Order(row['Row ID'],row['Order ID'], row['Order Date'], row['Ship Date'], row['Ship Mode'], row['Sales'])
            product = Product(row['Product ID'], row['Product Name'], row['Category'], row['Sub-Category'])
            customer = Customer(row['Customer ID'], row['Customer Name'], row['Segment'])
            location = Location(row['Country'], row['City'], row['State'], row['Postal Code'], row['Region'])

            order.product = product
            order.customer = customer
            order.location = location

            list_orders.append(order)

    
    # tranform and load
    
    start_function = time.time()
    
    [load_data.insert_into_customer(order) for order in list_orders]
    
    end_function = time.time()
    print(f"Load customer has fineshed: {end_function-start_function} seconds")

    start_function = time.time()

    [load_data.insert_into_product(order) for order in list_orders]

    end_function = time.time()
    print(f"Load product has fineshed: {end_function-start_function} seconds")

    start_function = time.time()

    [load_data.insert_into_location(order) for order in list_orders]

    end_function = time.time()
    print(f"Load location has fineshed: {end_function-start_function} seconds")   

    start_function = time.time()

    [load_data.insert_int_fact_table(order) for order in list_orders]

    end_function = time.time()
    print(f"Load fact sales has fineshed: {end_function-start_function} seconds")  
