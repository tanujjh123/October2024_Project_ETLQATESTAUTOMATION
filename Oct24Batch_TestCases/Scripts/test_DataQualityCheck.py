import pandas as pd
import pytest
from sqlalchemy import create_engine
#from test_ExtrcationTestCase import connect_to_oracle_SRC
import cx_Oracle

#1. Data type check
@pytest.fixture()
def connect_to_oracle_SRC():
    engine = create_engine("oracle+cx_oracle://system:admin@localhost:1521/xe")
    connection_oracle = engine.connect()
    yield connection_oracle
    connection_oracle.close()


@pytest.fixture()
def connect_to_mysql_TGT():
    engine = create_engine("mysql+pymysql://root:Admin%40143@localhost:3308/etlautomation")
    connection_mysql = engine.connect()
    yield connection_mysql
    connection_mysql.close()

def test_DQ_DataTypeCheck(connect_to_oracle_SRC):
    query = 'select * from emp'
    df_actual = pd.read_sql(query,connect_to_oracle_SRC)
    #print("Data Type from source: ",df_actual.dtypes)
    #df_expected_dict = {"name":"object","id":"int64"}
    #df_expected_dict = {"name": "object"}
    #assert df_actual.dtypes.to_dict() == df_expected_dict,"Data type mismatch"


#2. Referential Integerity ( foreign key )

def test_DQ_referentialIntegrity_check(connect_to_mysql_TGT):
    query_parent_country = """select country_name from country;"""
    query_child_city = """select country from city"""
    df_parent  = pd.read_sql(query_parent_country,connect_to_mysql_TGT)
    df_child = pd.read_sql(query_child_city, connect_to_mysql_TGT)
    print("Data from parent table ",df_parent)
    print("==================================")
    print("Data from child table ", df_child)
    valid = df_child['country'].isin(df_parent['country_name'])
    invalid = ~valid
    extra_data_df=df_child[invalid]
    extra_data_df.to_csv("extra_data.csv",index=False)
    assert extra_data_df.empty," referential integerity violation"

#3. Duplicate check



