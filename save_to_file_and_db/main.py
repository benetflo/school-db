from app.api import get_futurama_characters
from app.api import get_futurama_episodes

from app.file_storage import store_character_files
from app.file_storage import store_episodes_files

from app.mongo_db_storage import store_characters_in_mongodb

from app.mysql_storage import store_characters_in_mysql
from app.mysql_storage import store_episodes_in_mysql

def main():
	character_data = get_futurama_characters()
	episodes_data = get_futurama_episodes()

	if character_data:
		store_character_files(character_data)
		store_characters_in_mongodb(character_data)
		store_characters_in_mysql(character_data)

	if episodes_data:
		store_episodes_files(episodes_data)
		store_characters_in_mongodb(episodes_data)
		store_episodes_in_mysql(episodes_data)

if __name__ == "__main__":
	main()
