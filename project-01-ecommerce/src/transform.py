import pandas as pd
import numpy as np
from extract import load_data

def transform():
    customers, orders, order_items, order_payments, order_reviews, products, sellers, geolocation, category_translation = load_data()

    # merge orders with customers
    df = orders.merge(customers, on='customer_id', how='left')

    # merge with order items
    df = df.merge(order_items, on='order_id', how='left')

    # merge with products
    df = df.merge(products, on='product_id', how='left')

    # get english category names
    df = df.merge(category_translation, on='product_category_name', how='left')

    # merge sellers
    df = df.merge(sellers, on='seller_id', how='left')

    print("merged shape:", df.shape)
    print(df.columns.tolist())

    return df


if __name__ == "__main__":
    df = transform()
    print(df.head())
