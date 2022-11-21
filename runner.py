
import pandas as pd

from etl.extract import table
from etl.transform import transform_body, transform_head
from etl.load import load_table


def run_etl():
    data = transform_head(table)
    data = transform_body(table)
    load_table(data)


run_etl()


df = pd.read_csv('database/fii_table.csv', sep=';')
print(df)
