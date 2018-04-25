import redis


def r():
	return redis.StrictRedis(host='localhost', port=6379, db=0)

def get_key(test):
	return f"ab:{test}"

def user_in_test(user_id, test):
	return r().sismember(get_key(test), user_id) 

def add_user_to_test(user_id, test):
	return r().sadd(get_key(test), user_id)

