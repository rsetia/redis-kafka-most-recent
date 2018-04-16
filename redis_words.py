import random
import redis
import time

current_milli_time = lambda: int(round(time.time() * 1000))

def r():
	return redis.StrictRedis(host='localhost', port=6379, db=0)

def get_key(user_id):
	return f"recent_words:{user_id}"

# zrevrange key N
def get_latest_words(user_id):
	return r().zrevrange(get_key(user_id), 0, 5)	

add_word_and_trim_script = None

def push_word_entry(user_id, word_entry):
	global add_word_and_trim_script

	if add_word_and_trim_script == None:
		lua = """
			local value = redis.call('ZADD', KEYS[1], ARGV[1], ARGV[2])
			redis.call('ZREMRANGEBYRANK', KEYS[1], 0, ARGV[3])
			value = tonumber(value)
			return value"""
		add_word_and_trim_script = r().register_script(lua)
	
	score = current_milli_time()
	member = word_entry
	max_size = -4
	return add_word_and_trim_script(keys=[get_key(user_id)], args=[score, member, max_size])


word_entry = { "foo" : random.choice("abcdefghijklmnopqrstuvwxyz") } 
print(push_word_entry(1, word_entry))
print(get_latest_words(1))
