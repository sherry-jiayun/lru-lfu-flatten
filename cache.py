import sys

# do boch least recently used cache
# and least frequence used cache 

class cache_lru(object):
	"""docstring for cache_lru"""
	def __init__(self, capacity):
		super(cache_lru, self).__init__()
		self.capacity = capacity

	def get(self,key):
		print ("Get function with key:",key)
		return 

	def put(self,key,value):
		print ("Put function with key:",key,"value:",value)
		return

	def insert(self,key,value,order):
		print ("Insert function with key:",key,"value:",value,"order:",order)
		return

	def search(self, value):
		print ("Search function with value:",value)
		return

	def startwith(self,start):
		print ("Start with function with start str:",start)
		return

class cache_lfu(object):
	"""docstring for cache_lfu"""
	def __init__(self, capacity):
		super(cache_lfu, self).__init__()
		self.capacity = capacity

	def get(self,key):
		print ("Get function with key:",key)
		return 

	def put(self,key,value):
		print ("Put function with key:",key,"value:",value)
		return

	def insert(self,key,value,order):
		print ("Insert function with key:",key,"value:",value,"order:",order)
		return

	def search(self, value):
		print ("Search function with value:",value)
		return

	def startwith(self,start):
		print ("Start with function with start str:",start)
		return

class flatten(object):
	"""docstring for flatten"""
	def __init__(self, list_str):
		super(flatten, self).__init__()
		self.list_str = list_str
		
	def hasNext(self):
		print ("Has Next function")

def lru_command():
	'''
	example command:
	get:1
	put:1 2
	insert:1 2 3
	search:2
	startwith:s
	'''
	var = input("Please enter command command:parameter0 parameter1 parameter2:\ne.g.[get|put|insert|search|startwith|exit]:[key|value|startstr] [value [order]]\n")
	lru_cache = cache_lru(2)
	while True:
		if var == 'exit': break
		varlist = var.split(':')
		if len(varlist) > 1:
			if varlist[0] == 'get' and len(varlist) == 2: lru_cache.get(varlist[1])
			if varlist[0] == 'put' and len(varlist) == 2 and len(varlist[1].split()) == 2: lru_cache.put(varlist[1].split()[0],varlist[1].split()[1])
			if varlist[0] == 'insert' and len(varlist) == 2 and len(varlist[1].split()) == 3: lru_cache.insert(varlist[1].split()[0],varlist[1].split()[1],varlist[1].split()[2])
			if varlist[0] == 'search' and len(varlist) == 2: lru_cache.search(varlist[1])
			if varlist[0] == 'startwith' and len(varlist) == 2: lru_cache.startwith(varlist[1])
		else: print ("Invalid command, try again!")
		var = input()

def flatten_command():
	'''
	e.g.[1,[4,[6]]]
	use stack
	'''
	var = input("Please enter the list:\n")
	f = flatten(var)
	f.hasNext()

def lfu_command():
	'''
	example command:
	get:1
	put:1 2
	insert:1 2 3
	search:2
	startwith:s
	'''
	var = input("Please enter command command:parameter0 parameter1 parameter2:\ne.g.[get|put|insert|search|startwith|exit]:[key|value|startstr] [value [order]]\n")
	lfu_cache = cache_lfu(2)
	while True:
		if var == 'exit': break
		varlist = var.split(':')
		if len(varlist) > 1:
			if varlist[0] == 'get' and len(varlist) == 2: lfu_cache.get(varlist[1])
			if varlist[0] == 'put' and len(varlist) == 2 and len(varlist[1].split()) == 2: lfu_cache.put(varlist[1].split()[0],varlist[1].split()[1])
			if varlist[0] == 'insert' and len(varlist) == 2 and len(varlist[1].split()) == 3: lfu_cache.insert(varlist[1].split()[0],varlist[1].split()[1],varlist[1].split()[2])
			if varlist[0] == 'search' and len(varlist) == 2: lfu_cache.search(varlist[1])
			if varlist[0] == 'startwith' and len(varlist) == 2: lfu_cache.startwith(varlist[1])
		else: print ("Invalid command, try again!")
		var = input()

if __name__ == "__main__":
	arg_list = sys.argv
	# print (arg_list)
	mode = arg_list[1] if len(arg_list) == 2 else exit(0)
	if mode == '1': 
		print ("LRU cache:")
		lru_command()
	if mode == '2': 
		print ("LFU cache:") 
		lfu_command()
	if mode == '3': 
		print ("Flatter:")
		flatten_command()

