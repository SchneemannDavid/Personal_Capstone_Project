import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import os
from env import user, password, host
 
def handle_nulls(df):    
    # We keep 97.8% of the data after dropping nulls
    # ((df.Cancelled == 0).sum() / df) = 0.9784
    df = df[df['ArrTime'].notna()]
    df = df.drop(columns='CancellationCode', axis =1)
    return df


def optimize_types(df):
    # Convert some columns to integers for optimization
    # All float columns can become integers
    df["DepTime"] = df["DepTime"].astype(int)
    df["ArrTime"] = df["ArrTime"].astype(int)
    df["ActualElapsedTime"] = df["ActualElapsedTime"].astype(int)
    df["CRSElapsedTime"] = df["CRSElapsedTime"].astype(int)
    df["ArrDelay"] = df["ArrDelay"].astype(int)
    df["DepDelay"] = df["DepDelay"].astype(int)
    df["AirTime"] = df["AirTime"].astype(int)
    return df

def clean_variables(df):
    # Rename columns and 'fips' values to reflect actual location (to solidify column as categorical variable)
    df = df.rename(columns = {'DayofMonth':'dayofmonth', 
                        'DayOfWeek':'weekday',
                        'DepTime':'depart', 
                        'CRSDepTime':'scheduled_depart', 
                        'ArrTime':'arrive', 
                        'CRSArrTime':'scheduled_arrive', 
                        'ActualElapsedTime':'total_time', 
                        'CRSElapsedTime':'scheduled_total_time'
                        })
    return df 

def feature_engineering(df):
    # Create feature that takes sum of `ArrDelay` & `DepDelay`; in minutes
    df['total_delay'] = (df['ArrDelay'] + df['DepDelay'])
    # Create feature of difference between actual total time and scheduled total time
    df['total_time_diff'] = df['total_time'] - df['scheduled_total_time']

    # Converting `total_delay` to integer dtype
    df["total_delay"] = df["total_delay"].astype(int)

    # Create var for creating dummies
    df['month'] = df['Month']
    # Create dummies for month column
    df = pd.get_dummies(df, prefix='month', columns=['month'])
    # Create var for creating dummies
    df['WEEKday'] = df['weekday']
    # Create dummies for weekday column
    df = pd.get_dummies(df, prefix='weekday', columns=['WEEKday'])
    # Create var for creating dummies
    df['carrier'] = df['UniqueCarrier']
    # Create dummies for weekday column
    df = pd.get_dummies(df, prefix='uniq_carr', columns=['carrier'])

    # Drop 'ArrDelay' & 'DepDelay' columns (variable has direct relationship with target variable)
    df = df.drop(columns='Year', axis =1)
    df = df.drop(columns='ArrDelay', axis =1)
    df = df.drop(columns='DepDelay', axis =1)
    df = df.drop(columns='CarrierDelay', axis =1)
    df = df.drop(columns='WeatherDelay', axis =1)
    df = df.drop(columns='NASDelay', axis =1)
    df = df.drop(columns='SecurityDelay', axis =1)
    df = df.drop(columns='LateAircraftDelay', axis =1)
    df = df.drop(columns='FlightNum', axis =1)
    df = df.drop(columns='TailNum', axis =1)
    df = df.drop(columns='Cancelled', axis =1)
    df = df.drop(columns='Diverted', axis =1)
    df = df.drop(columns='Dest', axis =1)

    return df

# ------------- Split for Exploration ------------- #

## 
# Train, Validate, Test Split Function: for exploration
def flight_delay_split_explore(df):
    '''
    This function performs split on telco data, stratifying on churn.
    Returns train, validate, and test dfs.
    '''
    train_validate, test = train_test_split(df, test_size=.2,
                                        random_state=123)
    train, validate = train_test_split(train_validate, test_size=.3,
                                   random_state=123)
    return train, validate, test

### ------------------------------------------------------------------------

# Split for Modeling: X & Y dfs
def flight_delay_split_model(df):
    '''
    This function performs split on telco data, stratifying on churn.
    Returns both X and y train, validate, and test dfs
    '''
    
    train_validate, test = train_test_split(df, test_size=.2,
                                        random_state=123)
    train, validate = train_test_split(train_validate, test_size=.3,
                                   random_state=123)

    # Splitting train, validate, and test dfs on x and y
    x_train = train.drop(columns=['total_delay'])
    x_validate = validate.drop(columns=['total_delay'])
    x_test = test.drop(columns=['total_delay'])

    y_train = train['total_delay']
    y_validate = validate['total_delay']
    y_test = test['total_delay']
    
    return x_train, y_train, x_validate, y_validate, x_test, y_test


def prep_flight_delay(df):
    """
    Handles nulls
    optimizes or fixes data types
    handles outliers w/ manual logic
    clean variables via dropping columns and renaming features
    includes feature engineering 
    returns a clean dataframe
    Splits df into train, validate, test, and associated dfs on x and y 
    """
    df = handle_nulls(df)

    df = optimize_types(df)

    df = clean_variables(df)

    df = feature_engineering(df)

    train, validate, test = flight_delay_split_explore(df)

    x_train, y_train, x_validate, y_validate, x_test, y_test = flight_delay_split_model(df)

    df.to_csv('~/codeup/external_data_tap/final_flight_delay.csv', index=False)

    return df, train, validate, test, x_train, y_train, x_validate, y_validate, x_test, y_test