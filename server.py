from multiprocessing import Process
import word_entry_consumer as consumer
import word_entry_producer as producer
import db
import redis_words
import time
import redis_ab as ab 


test = "word_entry_recent"

def get_recent_words(user_id):
	if ab.user_in_test(user_id, test):
		print("GET_RECENT: REDIS")
		recents = redis_words.get_latest_words(user_id)
		print(recents)
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
		word_entry = { "user_id": "1", "word": "orange" }
		db.insert_word(word_entry)

		result = get_recent_words(1)
		mapped = list(map(lambda x: x['created_at'].strftime("%Y-%m-%d:%H-%M-%S"), result))
		for i in mapped:
			print(i)
		time.sleep(2)

def main():
	consumer_process = Process(target=consumer.bootstrap)    
	consumer_process.start()
	run_process = Process(target=run)
	run_process.start()
	#consumer_process.join()
if __name__ == "__main__":
    main()



