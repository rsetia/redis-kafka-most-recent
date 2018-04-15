from kafka import KafkaProducer
from kafka.errors import KafkaError
import json

def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)

def on_send_error(excp):
    log.error('I am an errback', exc_info=excp)
    # handle exception

def produce_word_entry(user_id, word):
	producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda m: json.dumps(m).encode('ascii'))

	future = producer.send('word_entries', {'user_id': user_id, 'word': word}).add_callback(on_send_success).add_errback(on_send_error)

	# Block for 'synchronous' sends
	try:
   		record_metadata = future.get(timeout=10)
	except KafkaError:
    # Decide what to do if produce request failed...
		log.exception()
		pass
