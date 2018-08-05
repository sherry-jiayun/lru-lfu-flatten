import sys

# do boch least recently used cache
# and least frequence used cache 

class cache_node(object):
	def __init__(self,key,val):
		self.key = key
		self.val = val
		self.next = None
		self.pre =None

class cache_lru(object):
	"""docstring for cache_lru"""
	def __init__(self, capacity):
		super(cache_lru, self).__init__()
		self.capacity = capacity
		self.cache = dict()
		self.order_head = None
		self.order_tail = None

	def get(self,key):
		value = self.cache.get(key,None)
		if not value: print ("Key not found.")
		else: 
			print ("Key:",key,"Value:",value.val)
			self.__update_node__(key)
		self.__print_order__()
		return 

	def put(self,key,value):
		cn = self.cache.get(key,None)
		if not cn:
			if len(self.cache) == self.capacity: self.__remove_node__()
			self.__add_node__(key,value)
		else:
			cn.val = value
			self.__update_node__(key)
		self.__print_order__()
		return

	def __print_order__(self):
		tmp_head = self.order_head
		while tmp_head:
			print (tmp_head.key,":",tmp_head.val)
			tmp_head = tmp_head.next
		return

	def __add_node__(self,key,value):
		cn = cache_node(key,value)
		if not self.order_head and not self.order_tail:
			self.order_head = self.order_tail = cn
		else:
			self.order_head.pre = cn
			cn.next = self.order_head
			self.order_head.pre = cn
			self.order_head = cn
		self.cache[key] = cn
		return 

	def __update_node__(self,key):
		tmp_head = self.cache.get(key)
		if not tmp_head.pre and not tmp_head.next: return
		if tmp_head.pre and tmp_head.next: # in the middle
			tmp_head.pre.next = tmp_head.next
			tmp_head.next.pre = tmp_head.pre
		elif not tmp_head.next: # tail
			self.order_tail = tmp_head.pre
			self.order_tail.next = None
		if tmp_head.pre: # head 
			tmp_head.next = self.order_head
			self.order_head.pre = tmp_head
			self.order_head = tmp_head
			tmp_head.pre = None
		else: # already head 
			return
		return

	def __remove_node__(self):
		new_tail = self.order_tail.pre
		if new_tail:
			new_tail.next = None
		self.order_tail.pre = None
		self.cache.pop(self.order_tail.key,None)
		if not new_tail: 
			self.order_head = None
		self.order_tail = new_tail
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

class tire(object):
	def __init__(self):
		super(tire,self).__init__()

	def insert(self,key,value,index):
		print("Insert function with key:",key,"value:",value,"index:",index)
		return

	def search(self,key):
		print("Search function with key:",key)
		return

	def startwith(self,startstr):
		print("Startwith function search startstr:",startstr)
		return

class flatten(object):
	"""docstring for flatten"""
	def __init__(self, list_str):
		super(flatten, self).__init__()
		self.list_str = list_str
		self.list_str = self.list_str.replace('[',',')
		self.list_str = self.list_str.replace(']',',')
		self.flatten_list = [e for e in self.list_str.split(',') if len(e) > 0]
		self.head_point = 0
		self.length = len(self.flatten_list)
		
	def hasNext(self):
		ans = self.flatten_list[self.head_point] if self.head_point < self.length else None
		self.head_point += 1
		return ans

def lru_command():
	'''
	example command:
	get:1
	put:1 2
	'''
	var = input("Please enter command command:parameter0 parameter1 parameter2:\ne.g.[get|put|exit]:[key] [value [order]]\n")
	lru_cache = cache_lru(10)
	while True:
		if var == 'exit': break
		varlist = var.split(':')
		if len(varlist) > 1:
			if varlist[0] == 'get' and len(varlist) == 2: lru_cache.get(varlist[1])
			if varlist[0] == 'put' and len(varlist) == 2 and len(varlist[1].split()) == 2: lru_cache.put(varlist[1].split()[0],varlist[1].split()[1])
		else: print ("Invalid command, try again!")
		var = input()

def flatten_command():
	'''
	e.g.[1,[4,[6]]]
	use stack
	'''
	var = input("Please enter the list:\n")
	f = flatten(var)
	value = f.hasNext()
	while value:
		print (value,' ',end = '')
		value = f.hasNext()
	print ()

def lfu_command():
	'''
	example command:
	get:1
	put:1 2
	'''
	var = input("Please enter command command:parameter0 parameter1 parameter2:\ne.g.[get|put|exit]:[key] [value [order]]\n")
	lfu_cache = cache_lfu(2)
	while True:
		if var == 'exit': break
		varlist = var.split(':')
		if len(varlist) > 1:
			if varlist[0] == 'get' and len(varlist) == 2: lfu_cache.get(varlist[1])
			if varlist[0] == 'put' and len(varlist) == 2 and len(varlist[1].split()) == 2: lfu_cache.put(varlist[1].split()[0],varlist[1].split()[1])
		else: print ("Invalid command, try again!")
		var = input()
def tire_command():
	'''
	example command:
	insert:1 2 3
	search:2
	startwith:s
	'''
	var = input("Please enter command command:parameter0 parameter1 parameter2:\ne.g.[insert|search|startwith|exit]:[key|startstr] [value [order]]\n")
	t = tire()
	while True:
		if var == 'exit': break
		varlist = var.split(':')
		if len(varlist) > 1:
			if varlist[0] == 'insert' and len(varlist) == 2 and len(varlist[1].split()) == 3: t.insert(varlist[1].split()[0],varlist[1].split()[1],varlist[1].split()[2])
			if varlist[0] == 'search' and len(varlist) == 2: t.search(varlist[1])
			if varlist[0] == 'startwith' and len(varlist) == 2: t.startwith(varlist[1])
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
	if mode == '4':
		print ("Tire:")
		tire_command()


