#!/usr/bin/env python
# coding: utf-8

#  #  A Whale off the Port(folio)
#  ---
# 
#  In this assignment, you'll get to use what you've learned this week to evaluate the performance among various algorithmic, hedge, and mutual fund portfolios and compare them against the S&P TSX 60 Index.

# In[1047]:


# Initial imports
get_ipython().system('pip install pandas')
import pandas as pd
import numpy as np
import datetime as dt
from pathlib import Path

get_ipython().run_line_magic('matplotlib', 'inline')


# # Data Cleaning
# 
# In this section, you will need to read the CSV files into DataFrames and perform any necessary data cleaning steps. After cleaning, combine all DataFrames into a single DataFrame.
# 
# Files:
# 
# * `whale_returns.csv`: Contains returns of some famous "whale" investors' portfolios.
# 
# * `algo_returns.csv`: Contains returns from the in-house trading algorithms from Harold's company.
# 
# * `sp_tsx_history.csv`: Contains historical closing prices of the S&P TSX 60 Index.

# ## Whale Returns
# 
# Read the Whale Portfolio daily returns and clean the data.

# In[1048]:


wr_path = ("Resources/whale_returns.csv")


# In[1049]:


wr = pd.read_csv("whale_returns.csv", parse_dates=True, infer_datetime_format=True)


# In[1050]:


wr = wr.set_index("Date")


# In[1051]:


# Reading whale returns
wr.head()


# In[1052]:


# Count nulls
wr.isnull().sum()


# In[1053]:


# Drop nulls
wr = wr.dropna().copy()
wr.isnull().sum()


# In[ ]:





# ## Algorithmic Daily Returns
# 
# Read the algorithmic daily returns and clean the data.

# In[1054]:


# Reading algorithmic returns
algo_returns_path = ("Resources/algo_returns.csv")
ar = pd.read_csv("algo_returns.csv", parse_dates=True, infer_datetime_format=True)
ar = ar.set_index("Date")


# In[1055]:


ar.head()


# In[1056]:


# Count nulls
ar.isnull().sum()


# In[1057]:


# Drop nulls
ar = ar.dropna().copy()
ar.isnull().sum()


# In[ ]:





# ## S&P TSX 60 Returns
# 
# Read the S&P TSX 60 historic closing prices and create a new daily returns DataFrame from the data. 

# In[1058]:


# Reading S&P TSX 60 Closing Prices
sp_tsx_history_path = ("../Resources/sp_tsx_history.csv")
sph = pd.read_csv("sp_tsx_history.csv", parse_dates=True, index_col="Date",infer_datetime_format=True)



# In[1059]:


sph.head()


# In[1060]:


# Check Data Type
sph.info()


# In[1061]:


sph["Close"].dtype


# In[1062]:


# Fix Data Types
sph["Close"] = sph["Close"].str.replace("$", "", regex=True)
sph["Close"] = sph["Close"].str.replace(",", "", regex=True)
sph["Close"].head(10)


# In[1063]:


sph["Close"] = sph["Close"].astype("float")
sph["Close"].dtype


# In[1064]:


# Calculate Daily Returns 
sph_returns = sph.pct_change()
                


# In[1065]:



sph_returns.head(10)    


# In[1066]:


# Drop nulls

sph_returns = sph_returns.dropna().copy()


# In[1067]:


# Rename `Close` Column to be specific to this portfolio.

sph_returns = sph_returns.rename(columns={'Close':'s&p_tsx'})


# In[1068]:



sph_returns.head()


# ## Combine Whale, Algorithmic, and S&P TSX 60 Returns

# In[1070]:


# Join Whale Returns, Algorithmic Returns, and the S&P TSX 60 Returns into a single DataFrame with columns for each portfolio's returns.
was_returns_concat = pd.concat([wr, ar, sph_returns], axis = "columns", join = "outer")
was_returns_concat.head()



# In[ ]:





# 
# 
# ---

# # Conduct Quantitative Analysis
# 
# In this section, you will calculate and visualize performance and risk metrics for the portfolios.

# ## Performance Anlysis
# 
# #### Calculate and Plot the daily returns.

# In[881]:


# Plot daily returns of all portfolios
was_returns_concat.plot(kind="line", title="Portfolio Daily Returns", figsize=(20,10))


# #### Calculate and Plot cumulative returns.

# In[831]:


# Calculate cumulative returns of all portfolios

# Plot cumulative returns


# ---

# ## Risk Analysis
# 
# Determine the _risk_ of each portfolio:
# 
# 1. Create a box plot for each portfolio. 
# 2. Calculate the standard deviation for all portfolios.
# 4. Determine which portfolios are riskier than the S&P TSX 60.
# 5. Calculate the Annualized Standard Deviation.

# ### Create a box plot for each portfolio
# 

# In[ ]:


# Box plot to visually show risk


# ### Calculate Standard Deviations

# In[ ]:


# Calculate the daily standard deviations of all portfolios


# ### Determine which portfolios are riskier than the S&P TSX 60

# In[ ]:


# Calculate  the daily standard deviation of S&P TSX 60

# Determine which portfolios are riskier than the S&P TSX 60


# ### Calculate the Annualized Standard Deviation

# In[ ]:


# Calculate the annualized standard deviation (252 trading days)


# ---

# ## Rolling Statistics
# 
# Risk changes over time. Analyze the rolling statistics for Risk and Beta. 
# 
# 1. Calculate and plot the rolling standard deviation for for all portfolios using a 21-day window.
# 2. Calculate the correlation between each stock to determine which portfolios may mimick the S&P TSX 60.
# 3. Choose one portfolio, then calculate and plot the 60-day rolling beta for it and the S&P TSX 60.

# ### Calculate and plot rolling `std` for all portfolios with 21-day window

# In[ ]:


# Calculate the rolling standard deviation for all portfolios using a 21-day window

# Plot the rolling standard deviation


# ### Calculate and plot the correlation

# In[ ]:


# Calculate the correlation

# Display de correlation matrix


# ### Calculate and Plot Beta for a chosen portfolio and the S&P 60 TSX

# In[ ]:


# Calculate covariance of a single portfolio

# Calculate variance of S&P TSX

# Computing beta

# Plot beta trend


# ## Rolling Statistics Challenge: Exponentially Weighted Average 
# 
# An alternative way to calculate a rolling window is to take the exponentially weighted moving average. This is like a moving window average, but it assigns greater importance to more recent observations. Try calculating the [`ewm`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.ewm.html) with a 21-day half-life.

# In[ ]:


# Use `ewm` to calculate the rolling window


# ---

# # Sharpe Ratios
# In reality, investment managers and thier institutional investors look at the ratio of return-to-risk, and not just returns alone. After all, if you could invest in one of two portfolios, and each offered the same 10% return, yet one offered lower risk, you'd take that one, right?
# 
# ### Using the daily returns, calculate and visualize the Sharpe ratios using a bar plot

# In[ ]:


# Annualized Sharpe Ratios


# In[ ]:


# Visualize the sharpe ratios as a bar plot


# ### Determine whether the algorithmic strategies outperform both the market (S&P TSX 60) and the whales portfolios.
# 
# Write your answer here!

# ---

# # Create Custom Portfolio
# 
# In this section, you will build your own portfolio of stocks, calculate the returns, and compare the results to the Whale Portfolios and the S&P TSX 60. 
# 
# 1. Choose 3-5 custom stocks with at last 1 year's worth of historic prices and create a DataFrame of the closing prices and dates for each stock.
# 2. Calculate the weighted returns for the portfolio assuming an equal number of shares for each stock.
# 3. Join your portfolio returns to the DataFrame that contains all of the portfolio returns.
# 4. Re-run the performance and risk analysis with your portfolio to see how it compares to the others.
# 5. Include correlation analysis to determine which stocks (if any) are correlated.

# ## Choose 3-5 custom stocks with at last 1 year's worth of historic prices and create a DataFrame of the closing prices and dates for each stock.

# In[ ]:


# Reading data from 1st stock


# In[ ]:


# Reading data from 2nd stock


# In[ ]:


# Reading data from 3rd stock


# In[ ]:


# Combine all stocks in a single DataFrame


# In[ ]:


# Reset Date index


# In[ ]:


# Reorganize portfolio data by having a column per symbol


# In[ ]:


# Calculate daily returns

# Drop NAs

# Display sample data


# ## Calculate the weighted returns for the portfolio assuming an equal number of shares for each stock

# In[ ]:


# Set weights
weights = [1/3, 1/3, 1/3]

# Calculate portfolio return

# Display sample data


# ## Join your portfolio returns to the DataFrame that contains all of the portfolio returns

# In[ ]:


# Join your returns DataFrame to the original returns DataFrame


# In[ ]:


# Only compare dates where return data exists for all the stocks (drop NaNs)


# ## Re-run the risk analysis with your portfolio to see how it compares to the others

# ### Calculate the Annualized Standard Deviation

# In[ ]:


# Calculate the annualized `std`


# ### Calculate and plot rolling `std` with 21-day window

# In[ ]:


# Calculate rolling standard deviation

# Plot rolling standard deviation


# ### Calculate and plot the correlation

# In[ ]:


# Calculate and plot the correlation


# ### Calculate and Plot the 60-day Rolling Beta for Your Portfolio compared to the S&P 60 TSX

# In[ ]:


# Calculate and plot Beta


# ### Using the daily returns, calculate and visualize the Sharpe ratios using a bar plot

# In[ ]:


# Calculate Annualized Sharpe Ratios


# In[ ]:


# Visualize the sharpe ratios as a bar plot


# ### How does your portfolio do?
# 
# Write your answer here!

# In[ ]:




