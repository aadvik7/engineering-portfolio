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

    # check everything loaded correctly
    print("customers:", customers.shape)
    print("orders:", orders.shape)
    print("order_items:", order_items.shape)
    print("order_payments:", order_payments.shape)
    print("order_reviews:", order_reviews.shape)
    print("products:", products.shape)
    print("sellers:", sellers.shape)
    print("geolocation:", geolocation.shape)
    print("category_translation:", category_translation.shape)

    return customers, orders, order_items, order_payments, order_reviews, products, sellers, geolocation, category_translation


if __name__ == "__main__":
    load_data()
