from kafka import KafkaConsumer
import json
import redis_ab as ab
import redis_words
from word_entry import WordEntry 

def bootstrap():
	consumer = KafkaConsumer('word_entries',
                         group_id='my-group',
                         bootstrap_servers=['localhost:9092'],
	value_deserializer=lambda m: json.loads(m.decode('ascii')))

	test = "word_entry_recent" 

	for message in consumer:
		#print ("CONSUMER: %s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
        #	                                  message.offset, message.key,
         #   	                              message.value))
	
		print(f"message.value: {message.value}")
		word_entry = WordEntry.from_json(message.value)
		user_id = word_entry.user_id

		if ab.user_in_test(user_id, test):
			print("CONSUMER: pushing")
			redis_words.push_word_entry(word_entry) 
