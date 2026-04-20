import pandas as pd
import os

DATA_PATH = "data/"

def load_data():
    customers = pd.read_csv(DATA_PATH + "olist_customers_dataset.csv")
    orders = pd.read_csv(DATA_PATH + "olist_orders_dataset.csv")
    order_items = pd.read_csv(DATA_PATH + "olist_order_items_dataset.csv")
    order_payments = pd.read_csv(DATA_PATH + "olist_order_payments_dataset.csv")
    order_reviews = pd.read_csv(DATA_PATH + "olist_order_reviews_dataset.csv", sep=';')
    products = pd.read_csv(DATA_PATH + "olist_products_dataset.csv")
    sellers = pd.read_csv(DATA_PATH + "olist_sellers_dataset.csv")
    geolocation = pd.read_csv(DATA_PATH + "olist_geolocation_dataset.csv")
    category_translation = pd.read_csv(DATA_PATH + "product_category_name_translation.csv")

    print(customers.shape)
    print(orders.shape)

    return customers, orders, order_items, order_payments, order_reviews, products, sellers, geolocation, category_translation
