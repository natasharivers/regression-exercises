import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
from pydataset import data
import math

from sklearn.model_selection import train_test_split
from scipy.stats import pearsonr, spearmanr
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.metrics import explained_variance_score

#####################FUNCTION TO PLOT RESIDUALS#####################

def plot_residuals(df, y, yhat):
    '''
    This function takes in actual value and predicted value 
    then creates a scatter plot
    '''
   #baseline
    df['yhat_baseline'] = df[y].mean()
    
    # residuals
    df['residuals'] = df[y] - df[yhat]
    df['baseline_residuals'] = df[y] - df['yhat_baseline']
    
    fig, ax = plt.subplots(figsize=(13, 7))
    ax.hist(df.baseline_residuals, label='baseline residuals', alpha=.6)
    ax.hist(df.residuals, label='model residuals', alpha=.6)
    ax.legend()
    return
    
#####################FUNCTION FOR REGRESSION ERRORS#####################

def regression_errors(y, yhat):
    '''
    This function takes in actual value and predicted value 
    then outputs: the sse, ess, tss, mse, and rmse
    '''
    residuals= y- yhat
    sse = (df.residuals **2).sum()
    ess= ((df.yhat - df.y.mean()) **2).sum()
    tss = ((df.y- df.y.mean())**2).sum()
    n = df.shape[0]
    mse = sse/n
    rmse = math.sqrt(mse)
        print(f''' 
        sse: {sse: .4f}
        ess: {ess: .4f}
        tss: {tss: .4f}
        mse: {mse: .4f}
        rmse: {rmse: .4f}
        ''')

#####################FUNCTION FOR BASELINE ERRORS#####################

def baseline_mean_errors(y):
    '''
    This function takes in actual value and predicted value
    then outputs: the SSE, MSE, and RMSE for the baseline model
    '''
    residuals= y- yhat
    sse_baseline = (df.residuals **2).sum()
    n = df.shape[0]
    mse_baseline = sse/n
    rmse_baseline = math.sqrt(mse_baseline)
        print(f''' 
        sse_baseline: {sse_baseline: .4f}
        mse_baseline: {mse_baseline: .4f}
        rmse_baseline: {rmse_baseline: .4f}
        ''')

##################FUNCTION TO RETURN BETTER THAN BASELINE##################

def better_than_baseline(y, yhat):
    '''
    This function takes in actual value and predicted value
    then returns true if your model performs better than the baseline, otherwise false
    '''
    if rmse < rmse_baseline:
        return True
    else:
        return False


