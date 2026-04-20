import pandas as pd
import os

DATA_PATH = "data/"

def load_data():
    customers = pd.read_csv(DATA_PATH + "olist_customers_dataset.csv")
    orders = pd.read_csv(DATA_PATH + "olist_orders_dataset.csv")
    order_items = pd.read_csv(DATA_PATH + "olist_order_items_dataset.csv")

    print(customers.shape)
    print(orders.shape)

    return customers, orders, order_items
