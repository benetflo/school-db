from app.api import get_futurama_characters
from app.file_storage import store_character_files
from app.mongo_db_storage import store_characters_in_mongodb
from app.mysql_storage import store_characters_in_mysql

def main():
	character_data = get_futurama_characters()
	if character_data:
		store_character_files(character_data)
		store_characters_in_mongodb(character_data)
		store_characters_in_mysql(character_data)

if __name__ == "__main__":
	main()
