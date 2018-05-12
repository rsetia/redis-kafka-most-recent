from multiprocessing import Process
import word_entry_consumer as consumer
import word_entry_producer as producer
import db
import redis_words
import time
import datetime
import redis_ab as ab 
from word_entry import WordEntry
from flask import Flask
from flask import request
from flask import jsonify

test = "word_entry_recent"

def get_recent_words(user_id):
	if ab.user_in_test(user_id, test):
		print("GET_RECENT: REDIS")
		recents = redis_words.get_latest_words(user_id)
		return recents
	else:
		print("GET_RECENT: DB")
		recents =  db.get_recent_words(user_id) 
		for r in reversed(recents): 
			redis_words.push_word_entry(r)	
		ab.add_user_to_test(user_id, test)
		return recents

def run():
	while 1:
		word_entry = WordEntry(None, "1", "orange", datetime.datetime.utcnow())
		word_entry = db.insert_word(word_entry)
		producer.produce_word_entry(word_entry)

		result = get_recent_words(1)
		mapped = list(map(lambda x: x.entered_at, result))
		for i in mapped:
			print(i)
		time.sleep(2)

def main():
	consumer_process = Process(target=consumer.bootstrap)    
	consumer_process.start()
	run_process = Process(target=run)
	run_process.start()
	#consumer_process.join()

# main()
app = Flask(__name__)
@app.route('/words/recent', methods=['GET'])
def hello_world():
	user_id = request.headers["user_id"]
	recents = get_recent_words(user_id)
	return jsonify(list(map(lambda x: x.to_obj(), recents)))

@app.route('/words', methods=['POST'])
def create_word():
	content = request.get_json()
	print(content)
	user_id = content['user_id']
	word = content['word']
	entered_at = datetime.datetime.strptime(content['entered_at'], "%Y-%m-%dT%H:%M:%S")
	word_entry = WordEntry(None, user_id, word, entered_at)
	db.insert_word(word_entry)
	producer.produce_word_entry(word_entry)
	return ""
	
