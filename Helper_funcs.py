import numpy as np
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
    return [lower_bound, IQR, upper_bound]

def unfinished_function(df):
    Average_temp = df["T_gem"].sort_values()
    size = len(df)
    Q1_index = int(size / 4)
    Q2_index = int(size / 2)
    Q3_index = int(size - Q1_index)

    TF_averageQ1 = Average_temp.iloc[:Q1_index]
    TF_averageQ2 = Average_temp.iloc[Q1_index:Q2_index]
    TF_averageQ3 = Average_temp.iloc[Q2_index:Q3_index]
    TF_averageQ4 = Average_temp.iloc[Q3_index:]

    maxQ1 = max(TF_averageQ1)
    maxQ3 = max(TF_averageQ3)

    IQR = (maxQ3 - maxQ1)
    quantiles = df.quantile([.25, .5, .75], axis = 0).reset_index()

def detect_outliers_tukey(x, k=1.5):
    q1 = np.percentile(x, 25)
    q3 = np.percentile(x, 75)
    iqr = q3 - q1
    fence_low = q1 - k * iqr
    fence_high = q3 + k * iqr
    outliers = (x < fence_low) | (x > fence_high)
    return outliers