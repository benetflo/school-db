import os
import json

def store_character_files(character_data):
	os.makedirs("output/characters", exist_ok=True)

	for character in character_data:
		with open(f"output/characters/{character['id']}.json", "w", encoding='utf-8') as f:
			json.dump(character, f, indent=2)

	print("Saved character data to output/characters directory")

def store_episodes_files(data):
	os.makedirs("output/episodes", exist_ok=True)

	for episode in data:
		with open(f"output/episodes/{episode['id']}.json", "w", encoding='utf-8') as f:
			json.dump(episode, f, indent=2)

	print("Saved episodes data to output/episodes directory")
