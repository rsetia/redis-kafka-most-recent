import random
import redis
import time
import json
import datetime
from word_entry import WordEntry

current_milli_time = lambda: int(round(time.time() * 1000))

def r():
	return redis.StrictRedis(host='localhost', port=6379, db=0)

def get_key(user_id):
	return f"recent_words:{user_id}"

def get_latest_words(user_id):
	return list(map(lambda x: WordEntry.from_json(x), r().zrevrange(get_key(user_id), 0, 5)))

add_word_and_trim_script = None

def push_word_entry(word_entry):
	global add_word_and_trim_script

	if add_word_and_trim_script == None:
		lua = """
			local value = redis.call('ZADD', KEYS[1], ARGV[1], ARGV[2])
			redis.call('ZREMRANGEBYRANK', KEYS[1], 0, ARGV[3])
			value = tonumber(value)
			return value"""
		add_word_and_trim_script = r().register_script(lua)
	
	key = get_key(word_entry.user_id)
	score = current_milli_time()
	member = word_entry.to_json()
	max_size = 3 
	trim = -1 * (max_size + 1)
	return add_word_and_trim_script(keys=[key], args=[score, member, trim])
