### BEGIN SOLUTION
def standardize_df(df):
    '''Standardize all the columns except the last one (target values).'''
    df_scaled = (df-df.mean())/df.std()
    df_scaled.iloc[:, -1] = df.iloc[:, -1]
    return df_scaled
### END SOLUTION