import pandas
import pandas as pd
import matplotlib as plt
import seaborn as sns
import os


def read_csv(filename, names):
    return pd.read_csv(filename,
                       comment='#',  # Skip all comments
                       header=None,  # No header
                       names=names,
                       skipinitialspace=True,  # Fix the trailing spaces after the ','-separator
                       index_col=[0, 1],  # Use the first two columns as the row index
                       parse_dates=[1])  # Let pandas try and transform the second column to a date


def calculate_iqr(data_series: pandas.Series) -> float:
    """"
    Method for calculating the Interquartile range for a pandas data series
    :param data_series: Pandas Data series
    :returns float
    """
    Q1 = data_series.describe()['25%']
    Q3 = data_series.describe()['75%']
    IQR = Q3 - Q1
    return IQR


def calculate_tukey(data_series) -> pd.tseries:
    """"
    Calculates the tukey analysis on a time series
    :param data_series: Pandas Data series
    :returns pandas data series
    """
    df = pd.DataFrame()
    Q1 = data_series.describe()['25%']
    Q3 = data_series.describe()['75%']
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return [lower_bound,IQR,upper_bound]
    # outliers = df[(df['TG'] < lower_bound) | (df['TG'] > upper_bound)]