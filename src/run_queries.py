from pathlib import Path
import argparse
import sqlite3
import pandas as pd


def run_queries(database, sql_dir='sql', output_dir='reports'):
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(database) as conn:
        for sql_file in sorted(Path(sql_dir).glob('*.sql')):
            query = sql_file.read_text(encoding='utf-8')
            df = pd.read_sql_query(query, conn)
            df.to_csv(out / f'{sql_file.stem}.csv', index=False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--database', default='data/business_demo.sqlite')
    parser.add_argument('--sql-dir', default='sql')
    parser.add_argument('--output-dir', default='reports')
    args = parser.parse_args()
    run_queries(args.database, args.sql_dir, args.output_dir)
    print(f'Reports saved to {args.output_dir}')


if __name__ == '__main__':
    main()
