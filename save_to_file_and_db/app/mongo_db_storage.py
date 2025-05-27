from pymongo import MongoClient

def store_characters_in_mongodb(character_data):
	mongo_client = MongoClient("mongodb://localhost:1337")
	mongo_db = mongo_client["futurama"]
	mongo_col = mongo_db["characters"]
	mongo_col.delete_many({})
	mongo_col.insert_many(character_data)

	print("Saved character data to MongoDB.")
