import csv
import pandas as pd

mdf = pd.read_csv('movies.csv')

mdf['year'] = mdf['title'].str.extract('\((\d{4})\)', expand=False)

mdf['year'] = pd.to_numeric(mdf['year'], errors='coerce').astype('Int64')

moviesYear = mdf

moviesYear.to_csv('moviesImproved.csv',index=False, quoting=csv.QUOTE_NONNUMERIC)

