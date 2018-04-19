from multiprocessing import Process
import word_entry_consumer as consumer
import word_entry_producer as producer
import db
import redis_words
import time

def run():
	while 1: 
		print("bar")
		word_entry = { "user_id": "1", "word": "orange" }
		db.insert_word(word_entry)
		redis_words.push_word_entry(word_entry)
		producer.produce_word_entry(word_entry)
#		result = db.get_recent_words(1) 
#		mapped = list(map(lambda x: x['created_at'], result))
#		print(mapped)
		time.sleep(2)

def main():
	print("foo")
	consumer_process = Process(target=consumer.bootstrap)    
	consumer_process.start()
	run_process = Process(target=run)
	run_process.start()
	#consumer_process.join()
	print("foo")
if __name__ == "__main__":
    main()



