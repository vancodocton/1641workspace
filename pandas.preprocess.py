# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# import library
import pandas
import numpy


# %%
# assign directory
dir_name = './datasets/'
file_name = 'preprocessed.onuni.FinanceAccounting.csv'

# load dataframe
df = pandas.read_csv(dir_name + file_name, encoding="utf-8", nrows=None)


# %%
# check the inputted dataframe
df.head()


# %%
df.hist(figsize=(25,15))


# %%
df.groupby('discount').mean()['rating'].plot(x='discount', y='rating', kind='line', figsize=(40,10))


# %%
df.groupby('discount_percent')['rating'].mean().plot(x='rating', y='discount_percent', figsize =(30,10))


