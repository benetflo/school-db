import mysql.connector

def connect_to_mysql():
	conn = mysql.connector.connect(
		host="localhost", user="user", password="password", database="futurama", port=3306
	)
	cursor = conn.cursor()
	return conn, cursor

def reset_table(cursor, name):
	cursor.execute(f"DROP TABLE IF EXISTS {name}")
	if name == "characters":
		cursor.execute(f"""
		CREATE TABLE {name} ( 
			id INT PRIMARY KEY,
			first_name VARCHAR(100),
			last_name VARCHAR(100),
			image_url TEXT
		)
		""")
	else:
		cursor.execute(f"""
		CREATE TABLE {name} (
			id INTEGER PRIMARY KEY,
			number TEXT,
			title TEXT,
			writers TEXT,
			originalAirDate TEXT,
			description TEXT
		)
		""")

def insert_characters(character_data, conn, cursor):

	for character in character_data:
		cursor.execute("INSERT INTO characters (id, first_name, last_name, image_url) VALUES (%s, %s, %s, %s)",
			(
				character["id"],
				character["name"]["first"],
				character["name"]["last"],
				character["images"]["main"],
			),
	)
	conn.commit()
	print("Saved character data to MySQL.")

def insert_episodes(data, conn, cursor):

	for key in data:
		cursor.execute("INSERT INTO episodes (id, number, title, writers, originalAirDate, description) VALUES (%s, %s, %s, %s, %s, %s)",
			(
				key["id"],
				key["number"],
				key["title"],
				key["writers"],
				key["originalAirDate"],
				key["desc"],
			),
	)
	conn.commit()
	print("Saved episodes data to MySQL")

def store_characters_in_mysql(data):
	conn, cursor = connect_to_mysql()
	reset_table(cursor, "characters")
	insert_characters(data, conn, cursor)
	cursor.close()
	conn.close()
	print("Closed MySQL connection.")


def store_episodes_in_mysql(data):
        conn, cursor = connect_to_mysql()
        reset_table(cursor, "episodes")
        insert_episodes(data, conn, cursor)
        cursor.close()
        conn.close()
        print("Closed MySQL connection.")
