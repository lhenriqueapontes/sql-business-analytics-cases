from pathlib import Path
import argparse
import sqlite3
import numpy as np
import pandas as pd


def build_tables(rows=1000, seed=42):
    rng = np.random.default_rng(seed)
    customers = pd.DataFrame({
        'customer_id': range(1, 101),
        'segment': rng.choice(['small', 'medium', 'enterprise'], 100),
        'region': rng.choice(['north', 'south', 'east', 'west'], 100),
    })
    products = pd.DataFrame({
        'product_id': range(1, 21),
        'product_name': [f'Product {i}' for i in range(1, 21)],
        'category': rng.choice(['software', 'service', 'training'], 20),
    })
    orders = pd.DataFrame({
        'order_id': range(1, rows + 1),
        'order_date': pd.date_range('2025-01-01', periods=rows, freq='D').astype(str),
        'customer_id': rng.integers(1, 101, rows),
        'product_id': rng.integers(1, 21, rows),
        'quantity': rng.integers(1, 8, rows),
        'unit_price': rng.normal(250, 70, rows).round(2),
    })
    orders['revenue'] = (orders['quantity'] * orders['unit_price']).round(2)
    return customers, products, orders


def create_database(output, rows=1000):
    out = Path(output)
    out.parent.mkdir(parents=True, exist_ok=True)
    customers, products, orders = build_tables(rows)
    with sqlite3.connect(out) as conn:
        customers.to_sql('customers', conn, if_exists='replace', index=False)
        products.to_sql('products', conn, if_exists='replace', index=False)
        orders.to_sql('orders', conn, if_exists='replace', index=False)
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='data/business_demo.sqlite')
    parser.add_argument('--rows', type=int, default=1000)
    args = parser.parse_args()
    print(create_database(args.output, args.rows))


if __name__ == '__main__':
    main()
