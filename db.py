import pymysql.cursors
import word_entry_producer as producer

# Connect to the database
def get_connection():
	connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='main',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
	return connection

def insert_word(user_id, word):
	connection = get_connection()
	with connection.cursor() as cursor:
		# Create a new record
		sql = "INSERT INTO `word_entries` (`user_id`, `word`) VALUES (%s, %s)"
		cursor.execute(sql, (user_id, word))
		connection.commit()
		producer.produce_word_entry(user_id, word)
	
	connection.close

def get_recent_words(user_id):
	connection = get_connection()
	with connection.cursor() as cursor:
		sql = "SELECT * FROM `word_entries` where `user_id` = %s order by `created_at` desc limit 10"
		cursor.execute(sql, (user_id, ))
		return cursor.fetchall()
	connection.close

