import pandas as pd
import pytest

def store_differences(actual, expected, file_path):
    # Finding rows that are different between actual and expected DataFrames
    diff = pd.concat([actual, expected]).drop_duplicates(keep=False)
    if not diff.empty:
        diff.to_csv(file_path, index=False)
    return diff


# Test case name ( test method )
def test_employeesDataLoad():
    df_source = pd.read_csv('data/employee_source.csv')
    df_target = pd.read_csv('data/employee_target.csv')

    ''' way 1 
    if(df_source.equals(df_target)):
        print("matching")
    else:
        print("difrences")
        
        
        pytest.fail(" source and target doesn't match")
    '''

    differences = store_differences(df_source, df_target, 'D:/ETL Testing Training/TestCaseResult/differences.csv')

    # Optionally, print the differences
    if not differences.empty:
        print(f"Differences between actual and expected data are saved in 'differences.csv'")

    assert df_source.equals(df_target),"source and target doesn't match"