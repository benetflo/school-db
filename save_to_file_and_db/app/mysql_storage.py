import mysql.connector

def connect_to_mysql():
	conn = mysql.connector.connect(
		host="localhost", user="user", password="password", database="futurama", port=3306
	)
	cursor = conn.cursor()
	return conn, cursor

def reset_table(cursor):
	cursor.execute("DROP TABLE IF EXISTS characters")
	cursor.execute("""
	CREATE TABLE characters ( 
		id INT PRIMARY KEY,
		first_name VARCHAR(100),
		last_name VARCHAR(100),
		image_url TEXT
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


def store_characters_in_mysql(character_data):
	conn, cursor = connect_to_mysql()
	reset_table(cursor)
	insert_characters(character_data, conn, cursor)
	cursor.close()
	conn.close()
	print("Closed MySQL connection.")
