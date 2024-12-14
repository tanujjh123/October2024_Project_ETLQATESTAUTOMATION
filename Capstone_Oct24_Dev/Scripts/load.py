import pandas as pd
from sqlalchemy import create_engine
import cx_Oracle
import logging
import os

# Create Logs directory if it doesn't exist
if not os.path.exists('Logs'):
    os.makedirs('Logs')

# Configure logging
logging.basicConfig(
    filename='Logs/etlprocess.log',  # Log file name
    filemode='a',  # 'a' to append, 'w' to overwrite
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
    level=logging.DEBUG  # Set logging level to DEBUG for detailed logs
)
logger = logging.getLogger(__name__)

# Create MySQL engine
from Scripts.config import *
mysql_engine = create_engine(f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}')

def execute_query(engine, query):
    try:
        conn = engine.raw_connection()
        cursor = conn.cursor()
        logger.debug(f"Executing query: {query}")
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
        logger.info("Successfully executed query")
    except Exception as e:
        logger.error("An error occurred while executing query", exc_info=True)

def load_fact_sales():
    query = """INSERT INTO fact_sales(sales_id, product_id, store_id, quantity, total_sales, sale_date)
               SELECT sales_id, product_id, store_id, quantity, total_amount, sale_date FROM sales_with_details"""
    execute_query(mysql_engine, query)

def load_inventory_fact():
    query = """INSERT INTO fact_inventory SELECT * FROM staging_inventory"""
    execute_query(mysql_engine, query)

def load_inventory_levels_by_store():
    query = """INSERT INTO inventory_levels_by_store(store_id, total_inventory)
               SELECT store_id, total_inventory FROM aggregated_inventory_levels"""
    execute_query(mysql_engine, query)

def load_monthly_summary():
    query = """INSERT INTO monthly_sales_summary SELECT * FROM monthly_sales_summary_source"""
    execute_query(mysql_engine, query)

if __name__== '__main__':
    logger.info("Data load started ....")
    load_fact_sales()
    load_inventory_fact()
    load_inventory_levels_by_store()
    load_monthly_summary()
    logger.info("Data load finished ....")
