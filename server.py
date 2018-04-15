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
		sql = "SELECT * FROM `word_entries` where `user_id` = %s order by `created_at` desc limit 10"
		cursor.execute(sql, (user_id, ))
		return cursor.fetchall()

try:
	insert_word(connection, 1, "orange")
	result = get_recent_words(connection, 1) 
	mapped = list(map(lambda x: x['created_at'], result))
	print(mapped)
finally:
    connection.close()
