import pandas as pd
import numpy as np


#
# TODO:
# Load up the dataset, setting correct header labels.
#
# .. your code here ..
#df = pd.read_csv('~/courses/course-python-datascience-ms/DAT210x/Module2/Datasets/census.data', 
df = pd.read_csv('~/course-python-datascience-ms/DAT210x/Module2/Datasets/census.data', 
                 names=['education', 'age', 'capital-gain', 'race', 'capital-loss', 'hours-per-week', 'sex', 'classification'])



#
# TODO:
# Use basic pandas commands to look through the dataset... get a
# feel for it before proceeding! Do the data-types of each column
# reflect the values you see when you look through the data using
# a text editor / spread sheet program? If you see 'object' where
# you expect to see 'int32' / 'float64', that is a good indicator
# that there is probably a string or missing value in a column.
# use `your_data_frame['your_column'].unique()` to see the unique
# values of each column and identify the rogue values. If these
# should be represented as nans, you can convert them using
# na_values when loading the dataframe.
#
# .. your code here ..
df.dtypes # review types
#df.col.....unique() help to review things
df['capital-gain'] = pd.to_numeric(df['capital-gain'],errors='coerse')
df['capital-loss'] = pd.to_numeric(df['capital-loss'],errors='coerse')

df['capital-gain'] = df['capital-gain'].fillna(0)

#
# TODO:
# Look through your data and identify any potential categorical
# features. Ensure you properly encode any ordinal and nominal
# types using the methods discussed in the chapter.
#
# Be careful! Some features can be represented as either categorical
# or continuous (numerical). Think to yourself, does it generally
# make more sense to have a numeric type or a series of categories
# for these somewhat ambigious features?
#
# .. your code here ..



#
# TODO:
# Print out your dataframe
#
# .. your code here ..


