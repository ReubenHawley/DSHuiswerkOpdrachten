import pandas as pd
import matplotlib as plt
import seaborn as sns


def read_csv(filename, names):
    return pd.read_csv(filename,
                       comment='#',  # Skip all comments
                       header=None,  # No header
                       names=names,
                       skipinitialspace=True,  # Fix the trailing spaces after the ','-separator
                       index_col=[0, 1],  # Use the first two columns as the row index
                       parse_dates=[1])  # Let pandas try and transform the second column to a date
