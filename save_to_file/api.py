import requests

# skriv ut hur många karaktärer som finns i apiet

def get_futurama_characters():
	# hämta någonting
	response = requests.get("https://distansakademin.github.io/api/futurama/characters")

	# laddar in information som hämtats och tolkar den som json. blir till python dictionary
	character_data = response.json()

	return character_data

