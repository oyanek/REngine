from pymongo import MongoClient


# Create a MongoClient object
client = MongoClient('localhost',27017)

# Connect to the local MongoDB database
db = client['RENG']
movies = db['moviesImproved']

result = movies.find({'genres': {'$regex': '.*Action.*'}})

for doc in result:
    print(doc)