import pandas as pd
import numpy as np
import os
from env import user, password, host

def get_db_url(database):
    return f'mysql+pymysql://{user}:{password}@{host}/{database}'

"""
USAGE: 
Use `from wrangle import wrangle_flight_delay` at the top of your notebook.
This 
"""
def get_flight_data():
    """Seeks to read the cached 2007.csv first """
    filename = "2007.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        return get_new_flight_data()

def get_new_flight_data():
    """Returns a dataframe representing US flight data for 2007 """

    df = pd.read_csv('~/codeup/external_data_tap/unzipped_data/2007.csv') 

    return df

def wrangle_flight_delay():
    """
    Acquires flight data
    """
    df = get_flight_data()

    # df.to_csv("acquire_flight_delay.csv", index=False)

    return df