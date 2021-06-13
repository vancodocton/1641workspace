# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas


# %%
# assign directory
dir_name = './datasets/'
file_name = 'onuni.Business.csv'


# %%
# load dataframe
dir_name = './datasets/'
file_name = 'onuni.Business.csv'

coursesinfo_df = pandas.read_csv(dir_name + file_name, encoding="utf-8", nrows=None)
coursesinfo_df.info()


# %%
# drop unused columns
unusedcols = ['is_wishlisted',
            'price_detail__currency',
            'discount_price__currency',
            'price_detail__price_string',
            'discount_price__price_string',
            'rating']
coursesinfo_df = coursesinfo_df.drop(unusedcols, axis=1)
coursesinfo_df.info()


# %%
# replace null data in 'price_detail__amount' and 'discount_price__amount'
coursesinfo_df['price_detail__amount'] = coursesinfo_df['price_detail__amount'].apply(lambda x: 0 if pandas.isnull(x) else x) 
coursesinfo_df['discount_price__amount'] = coursesinfo_df['discount_price__amount'].apply(lambda x: 0 if pandas.isnull(x) else x)
coursesinfo_df.info()


# %%
coursesinfo_df.to_csv(dir_name + 'preprocessed' + file_name, encoding="utf-8")


