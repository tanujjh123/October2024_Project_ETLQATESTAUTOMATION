import pandas as pd
import pytest
from sqlalchemy import create_engine
import cx_Oracle

def get_differences(df_target,df_source,file_path):
    concat_df = pd.concat([df_target,df_source])
    diff_df = concat_df.drop_duplicates(keep=False)
    if not diff_df.empty:
        diff_df.to_csv(file_path,index=False)
    return diff_df

@pytest.fixture()
def employees_source_csv_file_path():
    return 'data/employee_source.csv'

@pytest.fixture()
def employees_target_csv_file_path():
    return 'data/employee_target.csv'

# Test case name # 1( test method )
@pytest.mark.smoke
def test_employeesDataLoad(employees_source_csv_file_path,employees_target_csv_file_path):
    df_source = pd.read_csv(employees_source_csv_file_path)
    df_target = pd.read_csv(employees_target_csv_file_path)
    difference_df = get_differences(df_target,df_source,'TestResult_Output/differences_employee.csv')
    if not difference_df.empty:
        print(f"There are diffrence in source ana target and saved in to 'data/differences.csv'")
    assert df_source.equals(df_target),"source and target doesn't match"



@pytest.fixture()
def employees_source_json_file_path():
    return 'data/employees_source.json'

@pytest.fixture()
def employees_target_json_file_path():
    return 'data/employees_target.json'

# Test case name # 2( To test json source and target )
@pytest.mark.smoke
def test_employees_json_DataLoad(employees_source_json_file_path,employees_target_json_file_path):
    df_source = pd.read_json(employees_source_json_file_path)
    df_target = pd.read_json(employees_target_json_file_path)
    difference_df = get_differences(df_target,df_source,'TestResult_Output/differences_employee_json.csv')
    if not difference_df.empty:
        print(f"There are diffrence in source ana target and saved in to 'differences_employee_json.csv'")
    assert df_source.equals(df_target),"source and target doesn't match"

# Test case name # 2( To test json source and target )
@pytest.mark.smoke
def test_employees_json_DataLoad(employees_source_json_file_path,employees_target_json_file_path):
    df_source = pd.read_json(employees_source_json_file_path)
    df_target = pd.read_json(employees_target_json_file_path)

    difference_df = get_differences(df_target,df_source,'TestResult_Output/differences_employee_json.csv')
    if not difference_df.empty:
        print(f"There are diffrence in source ana target and saved in to 'differences_employees_json.csv'")
    assert df_source.equals(df_target),"source and target doesn't match"




# Test case name # 3( db-2-db checks )
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


@pytest.mark.smoke
def test_dataExtrcationFromOracleToLoadintoMYSQL(connect_to_oracle_SRC,connect_to_mysql_TGT):
    query_orcl_src ="""select * from city order by id"""
    df_orcl_src = pd.read_sql(query_orcl_src,connect_to_oracle_SRC)
    print("source data :",df_orcl_src)
    query_mysql_tgt ="""select * from city order by id"""
    df_mysql_tgt = pd.read_sql(query_mysql_tgt, connect_to_mysql_TGT)
    print("target data :", df_mysql_tgt)
    difference_df = get_differences(df_mysql_tgt,df_orcl_src,'TestResult_Output/database.csv')
    if not difference_df.empty:
        print(f"There are diffrence in source ana target and saved in to 'TestResult_Output/database.csv'")
    assert df_orcl_src.equals(df_mysql_tgt),"source - oracle and target-mysql doesn't match"