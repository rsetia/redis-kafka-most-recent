import pymysql.cursors
import word_entry_producer as producer
import db

db.insert_word(1, "orange")
result = db.get_recent_words(1) 
mapped = list(map(lambda x: x['created_at'], result))
print(mapped)
