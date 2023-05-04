import argparse
from pymongo import MongoClient

client = MongoClient('localhost',27017)

db = client['RENG']
movies = db['movies']

def search_title(movieId=None, title=None):
    if movieId:
        movie = movies.find_one({'movieId': movieId})
        if movie:
            title = movie['title']
            print(f"Movie with ID {movieId} is '{title}'.")
        else:
            print(f"No movie found with ID {movieId}.")
    elif title:
        results = movies.find({'title': {'$regex': title, '$options': 'i'}})
        for movie in results:
            print(f"Movie with ID {movie['movieId']} is '{movie['title']}'.")
    else:
        print('Please provide either a movie ID or a title.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find a movie by movieId or title.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-i', '--movie_id', type=int, help='The ID of the movie to search for')
    group.add_argument('-t', '--title', type=str, help='The title of the movie to search for')
    args = parser.parse_args()

    search_title(args.movie_id, args.title)
