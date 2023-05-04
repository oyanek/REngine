import argparse
from pymongo import MongoClient

client = MongoClient('localhost',27017)

db = client['RENG']
movies = db['movies']

def search_title(movieId):
    movie = movies.find_one({'movieId': movieId})
    if movie:
        title = movie['title']
        print(f"Movie with ID {movieId} is '{title}'.")
    else:
        print(f"No movie found with ID {movieId}.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find a movie title by movieId.')
    parser.add_argument('movie_id', type=int, help='The ID of the movie to search for')
    args = parser.parse_args()

    search_title(args.movie_id)
