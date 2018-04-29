import pymysql.cursors
import word_entry_producer as producer
from word_entry import WordEntry 
 
# Connect to the database
def get_connection():
	connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='main',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
	return connection

def insert_word(word_entry):
	print(f"insert_word: {word_entry}")
	user_id = word_entry.user_id
	word = word_entry.word
	entered_at = word_entry.entered_at.strftime('%Y-%m-%dT%H:%M:%S')
	connection = get_connection()
	inserted_id = 0
	print(f"entered_at: {entered_at}")
	with connection.cursor() as cursor:
		# Create a new record
		sql = "INSERT INTO `word_entries` (`user_id`, `word`, `entered_at`) VALUES (%s, %s, %s)"
		cursor.execute(sql, (user_id, word, entered_at))
		word_entry.id = str(cursor.lastrowid)
		connection.commit()
	connection.close
	return word_entry

def get_recent_words(user_id):
	connection = get_connection()
	with connection.cursor() as cursor:
		sql = "SELECT id, user_id, word, entered_at FROM `word_entries` where `user_id` = %s order by `entered_at` desc limit 10"
		cursor.execute(sql, (user_id, ))
		items = cursor.fetchall()
	connection.close
	return list(map(lambda x: WordEntry(str(x["id"]), str(x["user_id"]), x["word"], x["entered_at"]),
		items))

