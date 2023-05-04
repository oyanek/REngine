import csv
import pandas as pd
from pymongo import MongoClient

#connect
client = MongoClient('localhost',27017)

#retrieve collections
db = client['RENG']
movies = db['movies']
ratings = db['ratings']

#iterate using cursor then store as DataFrame
ratings_cursor = ratings.find({'userId': {'$lte': 1000}})
ratings_df = pd.DataFrame(list(ratings_cursor))

movies_cursor = movies.find()
movies_df = pd.DataFrame(list(movies_cursor))

#merge DataFrames
movie_ratings = pd.merge(movies_df,ratings_df,on='movieId')

#pivot, rows=userId columns=movieId
movie_ratings_pivot = pd.pivot_table(movie_ratings, values='rating',index='userId', columns='movieId', fill_value=-1)

#create new csv
movie_ratings_pivot.to_csv('moviesandratings.csv')
