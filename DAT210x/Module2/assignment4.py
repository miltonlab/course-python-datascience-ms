import pandas as pd


# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
# .. your code here ..

df = pd.read_html('http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/count/1')
# list returned
df = df[0]

# TODO: Rename the columns so that they match the
# column definitions provided to you on the website
#
# .. your code here ..

cols_str = 'RK,PLAYER,TEAM,GP,G,A,PTS,+/-,PIM,PTS/G,SOG,PCT,GWG,PP.G,PP.A,SH.G,SH.A'
df.columns = cols_str.split(',')
# TODO: Get rid of any row that has at least 4 NANs in it
#
# .. your code here ..

df = df.dropna(axis=0, thresh=4)

# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
# .. your code here ..

df = df.drop_duplicates()

# TODO: Get rid of the 'RK' column
#
# .. your code here ..

df = df.drop(labels=['RK'], axis = 1)

# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
# .. your code here ..

df = df.reset_index(drop=True)

# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric

#df.GP = pd.to_numeric(df.GP, errors='coerce')
#
#In [51]: df.G = pd.to_numeric(df.G, errors='coerce')
#
#In [52]: df.A = pd.to_numeric(df.A, errors='coerce')
#
#In [53]: df.PTS = pd.to_numeric(df.PTS, errors='coerce')
#
#In [54]: df.+/- = pd.to_numeric(df.+/-, errors='coerce')
#  File "<ipython-input-54-1bf28563812f>", line 1
#    df.+/- = pd.to_numeric(df.+/-, errors='coerce')
#       ^
#SyntaxError: invalid syntax
#
#
#In [55]: df['+/-'] = pd.to_numeric(df['+/-'], errors='coerce')
#
#In [56]: df.PIM = pd.to_numeric(df.PIM, errors='coerce')
#
#In [57]: df['PTS/G'] = pd.to_numeric(df['PTS/G'], errors='coerce')
#
#In [58]: df.SOG = pd.to_numeric(df.SOG, errors='coerce')
#
#In [59]: df.PCT = pd.to_numeric(df.PCT, errors='coerce')
#
#In [60]: df.GWG = pd.to_numeric(df.GWG, errors='coerce')
#
#In [61]: df['PP.A'] = pd.to_numeric(df['PP.A'], errors='coerce')
#
#In [62]: df['PP.G'] = pd.to_numeric(df['PP.G'], errors='coerce')
#
#In [63]: df['SH.G'] = pd.to_numeric(df['SH.G'], errors='coerce')
#
#In [64]: df['SH.A'] = pd.to_numeric(df['SH.A'], errors='coerce')



# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.

