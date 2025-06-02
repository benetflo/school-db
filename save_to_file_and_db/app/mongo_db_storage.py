from pymongo import MongoClient

def store_characters_in_mongodb(data):
	mongo_client = MongoClient("mongodb://localhost:1337")
	mongo_db = mongo_client["futurama"]

	mongo_col = mongo_db["characters"]
	mongo_col.delete_many({})
	mongo_col.insert_many(data)

	print("Saved character data to MongoDB.")

def store_episodes_in_mongodb(data):
	mongo_client = MongoClient("mongodb://localhost:1337")
	mongo_db = mongo_client["futurama"]

	mongo_col = mongo_db["episodes"]
	mongo_col.delete_many({})
	mongo_col.insert_many(data)

	print("Saved episodes data to MongoDB.")
