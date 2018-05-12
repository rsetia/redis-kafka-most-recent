import datetime 
import json 

def myconverter(o):
	if isinstance(o, datetime.datetime):
		return o.strftime('%Y-%m-%dT%H:%M:%S')

class WordEntry:

	def to_obj(self):
		return {
			"id" : self._id,
			"user_id" : self._user_id,
			"word" : self._word,
			"entered_at" : self._entered_at
		}
	
	def to_json(self):
		obj = {
			"id" : self._id,
			"user_id" : self._user_id,
			"word" : self._word,
			"entered_at" : self._entered_at
		}
	
		return json.dumps(obj, default = myconverter)
	
	@staticmethod
	def from_json(json_str):
		obj = json.loads(json_str)
		entered_at = datetime.datetime.strptime(obj["entered_at"], '%Y-%m-%dT%H:%M:%S')
		return WordEntry(obj["id"], obj["user_id"], obj["word"], entered_at) 
	
	# id
	def set_id(self, id):
		if id == None or isinstance(id, str):
			self._id = id
		else:
			raise ValueError("id must be a string")

	def get_id(self):
		return self.id

	# user_id
	def set_user_id(self, user_id):
		if isinstance(user_id, str):
			self._user_id = user_id
		else:
			raise ValueError("user_id must be a string")

	def get_user_id(self):
		return self._user_id

	# word
	def set_word(self, word):
		if isinstance(word, str):
			self._word = word
		else:
			raise ValueError("word must be a string")

	def get_word(self):
		return self._word

	# entered_at
	def set_entered_at(self, entered_at):
		if isinstance(entered_at, datetime.datetime):
			self._entered_at = entered_at
		else:
			raise ValueError("entered_at must be a DateTime")

	def get_entered_at(self):
		return self._entered_at

	def __init__(self, id, user_id, word, entered_at):
		self.id = id
		self.user_id = user_id
		self.word = word
		self.entered_at = entered_at 
	
	id = property(get_id, set_id)
	user_id = property(get_user_id, set_user_id)
	word = property(get_word, set_word) 
	entered_at = property(get_entered_at, set_entered_at) 
