from kafka import KafkaConsumer
import json

def bootstrap():
	consumer = KafkaConsumer('word_entries',
                         group_id='my-group',
                         bootstrap_servers=['localhost:9092'],
	value_deserializer=lambda m: json.loads(m.decode('ascii')))

	for message in consumer:
		print ("CONSUMER: %s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
        	                                  message.offset, message.key,
            	                              message.value))

