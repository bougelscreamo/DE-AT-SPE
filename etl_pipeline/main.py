import pandas as pd
from sqlalchemy import create_engine
import os


def extract_data(csv_file):
    df = pd.read_csv(csv_file)
    return df


def transform_data(df):

    df["total_amount"] = df["price"] * df["quantity"]


    def get_category(product_id):
        if product_id >= 500 and product_id < 600:
            return "Electronics"
        elif product_id >= 600 and product_id < 700:
            return "Home Appliances"
        else:
            return "Other"

    df["category"] = df["product_id"].apply(get_category)
    return df


def load_data(df, db_file="sales.db"):
    engine = create_engine(f'sqlite:///{db_file}')
    df.to_sql("sales", engine, if_exists="replace", index=False)
    print(f"Data successfully loaded to {db_file}")

if __name__ == "__main__":

    file_path = "sales_data.csv"
    df = extract_data(file_path)


    df_transformed = transform_data(df)


    load_data(df_transformed)
