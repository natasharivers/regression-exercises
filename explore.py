########################## Tenure Function ##########################

def months_to_years(df):
    '''
    this function accepts the telco churn dataframe
    and returns a dataframe with a new feature in complete years of tenure
    '''
    df['tenure_years'] = (df.tenure/12).astype(int)
    return df


################### Plot Variable Pairs Function ##################

def plot_variable_pairs(df):
    columns = df[list(df.select_dtypes(exclude = 'O').columns)]
    sns.set(style='whitegrid', palette='muted')
    g = sns.PairGrid(columns)
    g = g.map(sns.regplot, line_kws={'color':'red'})

