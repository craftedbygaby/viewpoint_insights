import pandas as pd

def standardize_columns(df, column_dict):
    """Renames columns to snake_case English names."""
    df = df.rename(columns=column_dict)
    return df

def dropping_columns(df, columns_to_drop): 
    """Drops the specified columns.""" 
    df = df.drop(columns=columns_to_drop)
    return df

def string_formatting(df):
    """Strips leading and trailing whitespace and converts to lowercase for all string columns."""
    for col in df.columns:
        try:
            df[col] = df[col].str.strip().str.lower()
        except AttributeError:
            pass
    return df

def translate_values(df, column_name, translation_dict):
    """Translates values in a specified column using a provided translation dictionary."""
    df[column_name] = df[column_name].map(translation_dict)
    return df   

def concat_dfs(df_list):
    """Concatenates dataframes."""
    df_all = pd.concat(df_list, ignore_index=True)
    return df_all

def add_covid_flag(df):
    """Adds a covid_period column based on the year column."""
    def classify(year):
        if year <= 2019:
            return 'pre_covid'
        elif year <= 2021:
            return 'covid'
        else:
            return 'post_covid'
    
    df['covid_period'] = df['year'].apply(classify)
    return df