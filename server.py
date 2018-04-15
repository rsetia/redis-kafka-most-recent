import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='main',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def insert_word(connection, user_id, word):
	with connection.cursor() as cursor:
		# Create a new record
		sql = "INSERT INTO `word_entries` (`user_id`, `word`) VALUES (%s, %s)"
		cursor.execute(sql, (user_id, word))
		connection.commit()

def get_recent_words(connection, user_id):
	with connection.cursor() as cursor:
        # Read a single record
		sql = "SELECT * FROM `word_entries`"
		cursor.execute(sql)
		return cursor.fetchone()

try:
	insert_word(connection, 1, "orange")
	result = get_recent_words(connection, 1) 
	print(result)
finally:
    connection.close()
