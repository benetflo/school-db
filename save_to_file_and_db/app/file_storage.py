import os
import json

def store_character_files(character_data):
	os.makedirs("output/characters", exist_ok=True)

	for character in character_data:
		with open(f"output/characters/{character['id']}.json", "w", encoding='utf-8') as f:
			json.dump(character, f, indent=2)

	print("Saved character data to output/characters directory")
