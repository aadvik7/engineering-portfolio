import pandas as pd
from extract import load_data

def transform():
    """Merge all tables, handle nulls, fix dtypes, add derived columns."""
    customers, orders, order_items, order_payments, order_reviews, products, sellers, geolocation, category_translation = load_data()

    df = orders.merge(customers, on='customer_id', how='left')
    df = df.merge(order_items, on='order_id', how='left')
    df = df.merge(products, on='product_id', how='left')
    df = df.merge(category_translation, on='product_category_name', how='left')
    df = df.merge(sellers, on='seller_id', how='left')

    # handle nulls
    df['product_category_name_english'].fillna('unknown', inplace=True)
    df['product_weight_g'].fillna(df['product_weight_g'].median(), inplace=True)
    df['product_length_cm'].fillna(df['product_length_cm'].median(), inplace=True)
    df['product_height_cm'].fillna(df['product_height_cm'].median(), inplace=True)
    df['product_width_cm'].fillna(df['product_width_cm'].median(), inplace=True)
    df.dropna(subset=['price'], inplace=True)

    # fix date columns
    date_cols = [
        'order_purchase_timestamp',
        'order_approved_at',
        'order_delivered_carrier_date',
        'order_delivered_customer_date',
        'order_estimated_delivery_date'
    ]
    for col in date_cols:
        df[col] = pd.to_datetime(df[col])

    # derived columns
    df['delivery_days'] = (df['order_delivered_customer_date'] - df['order_purchase_timestamp']).dt.days
    df['order_total'] = df['price'] + df['freight_value']
    df['purchase_month'] = df['order_purchase_timestamp'].dt.to_period('M')
    df['purchase_dow'] = df['order_purchase_timestamp'].dt.day_name()

    return df


if __name__ == "__main__":
    df = transform()
    print(df.shape)
