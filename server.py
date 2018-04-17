import pymysql.cursors
import word_entry_producer as producer
import db
import redis_words

word_entry = { "user_id": "1", "word": "orange" }
db.insert_word(word_entry)
redis_words.push_word_entry(word_entry)
producer.produce_word_entry(word_entry)
result = db.get_recent_words(1) 
mapped = list(map(lambda x: x['created_at'], result))
print(mapped)
