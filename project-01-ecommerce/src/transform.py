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

    # handle nulls
    df['product_category_name_english'].fillna('unknown', inplace=True)
    df['product_weight_g'].fillna(df['product_weight_g'].median(), inplace=True)
    df['product_length_cm'].fillna(df['product_length_cm'].median(), inplace=True)
    df['product_height_cm'].fillna(df['product_height_cm'].median(), inplace=True)
    df['product_width_cm'].fillna(df['product_width_cm'].median(), inplace=True)

    df.dropna(subset=['price'], inplace=True)

    # fix date columns - they come in as strings
    date_cols = [
        'order_purchase_timestamp',
        'order_approved_at',
        'order_delivered_carrier_date',
        'order_delivered_customer_date',
        'order_estimated_delivery_date'
    ]
    for col in date_cols:
        df[col] = pd.to_datetime(df[col])

    # feature engineering
    df['delivery_days'] = (df['order_delivered_customer_date'] - df['order_purchase_timestamp']).dt.days
    df['order_total'] = df['price'] + df['freight_value']
    df['purchase_month'] = df['order_purchase_timestamp'].dt.to_period('M')
    df['purchase_dow'] = df['order_purchase_timestamp'].dt.day_name()

    print("after null handling:", df.shape)
    print("delivery_days sample:\n", df['delivery_days'].describe())

    return df


if __name__ == "__main__":
    df = transform()
    print(df.head())
