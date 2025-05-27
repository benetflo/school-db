from api import get_futurama_characters
from file_storage import store_character_files

def main():
	character_data = get_futurama_characters()
	if character_data:
		store_character_files(character_data)

if __name__ == "__main__":
	main()
