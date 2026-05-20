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
    df[column_name] = df[column_name].replace(translation_dict)
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

def add_continent_column(df, country_col, continent_mapping):
    """Adds a continent column based on the country column using a provided mapping dictionary."""
    df['continent'] = df[country_col].replace(continent_mapping)
    return df

def value_counts_by_column(df):
    """Prints value counts for each column in the dataframe."""
    for col in df.columns:
        print(f'=== {col} ===')
        print(df[col].value_counts())
        print()

def seasons_brazil(df, month_col):
    """Adds a season column based on the month column for Brazil."""
    seasons_dict = {'december' : 'summer', 'january' : 'summer', 'february' : 'summer', 
                    'march' : 'autumn', 'april' : 'autumn', 'may' : 'autumn', 
                    'june' : 'winter', 'july' : 'winter', 'august' : 'winter', 
                    'september' : 'spring',   'october' : 'spring', 'november' : 'spring'}
    df['season'] = df[month_col].replace(seasons_dict)
    return df
    