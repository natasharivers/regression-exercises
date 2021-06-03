######################### Acquire Telco Function ###########################

#import libraries
import pandas as pd
import numpy as np
import os
from pydataset import data

# acquire
from env import host, user, password


# Create helper function to get the necessary connection url.
def get_connection(db_name):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    '''
    from env import host, user, password
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'


#create function to retrieve telco_churn data with specific columns
def get_telco_data():
    '''
    This function reads in the Telco Churn data from the Codeup db
    and returns a pandas DataFrame with customer_id, monthly_charges, tenure, total_charges columns
    for customers who have 2-year contracts.
    '''
    
    sql_query = '''
    SELECT customer_id, monthly_charges, tenure, total_charges
    FROM customers
    WHERE contract_type_id LIKE '3'
    '''
    return pd.read_sql(sql_query, get_connection('telco_churn'))

