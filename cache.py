import sys

# do boch least recently used cache
# and least frequence used cache 

class cache_node(object):
	def __init__(self,key,val):
		self.key = key
		self.val = val
		self.next = None
		self.pre =None
		self.frequence = 1

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
		self.cache = dict()
		self.order_head = None
		self.order_tail = None

	def get(self,key):
		# key not exit
		cn = self.cache.get(key,None)
		if not cn: print("Key not exist.")
		else: 
			print ("Key:",key,"Value:",cn.val)
			self.__update_node__(key)
			self.__print_order__()
		return 

	def put(self,key,value):
		# key not exist 
		if key not in self.cache.keys(): 
			if len(self.cache) == self.capacity: self.__remove_node__()
			if len(self.cache) < self.capacity: self.__add_node__(key,value) # capacity = 0
		else:
			cn = self.cache.get(key)
			cn.val = value
			self.__update_node__(key)
		self.__print_order__()
		return

	def __print_order__(self):
		tmp_head = self.order_head
		while tmp_head:
			print (tmp_head.key,":",tmp_head.val,"frequence:",tmp_head.frequence)
			tmp_head = tmp_head.next
		return

	def __print_order_reverse__(self):
		tmp_tail = self.order_tail
		while tmp_tail:
			print (tmp_tail.key,":",tmp_tail.val,"frequence:",tmp_tail.frequence)
			tmp_tail = tmp_tail.pre
		return

	def __add_node__(self,key,value):
		cn = cache_node(key,value) # new cache node 
		self.cache[key] = cn # add to cache
		if not self.order_head and not self.order_tail: self.order_head = self.order_tail = cn
		else:
			position = self.order_head
			while position and position.frequence > cn.frequence: position = position.next
			if position == self.order_head:
				self.order_head.pre = cn
				cn.next = self.order_head
				self.order_head = cn
			elif not position: # tail
				self.order_tail.next = cn
				cn.pre = self.order_tail
				self.order_tail = cn
			else:
				position.pre.next = cn
				cn.pre = position.pre
				cn.next = position
				position.pre = cn
		return

	def __remove_node__(self):
		cn = self.order_tail
		if self.order_tail.pre: 
			self.order_tail.pre.next = None
		self.order_tail = self.order_tail.pre
		if self.order_head == cn: self.order_head = None # 1 capacity
		self.cache.pop(cn.key, None)
		return

	def __update_node__(self,key):
		cn = self.cache.get(key)
		cn.frequence += 1
		while cn.pre and cn.frequence >= cn.pre.frequence:
			cn_pre = cn.pre
			cn_next = cn.next
			cn.pre = cn.pre.pre
			if cn.pre: cn.pre.next = cn
			cn.next = cn_pre
			cn_pre.pre = cn
			cn_pre.next = cn_next
			if cn_next: cn_next.pre = cn_pre
			else: self.order_tail = cn_pre
		if not cn.pre and not self.order_head == cn: self.order_head = cn # update tail
		return

class tire(object):
	def __init__(self):
		super(tire,self).__init__()
		self.head = None
		self.tail = None
		self.tmpPointer = None

	def insert(self,key,value):
		print("Insert function with key:",key,"value:",value)
		cn = cache_node(key,value)
		if not self.head: self.head = self.tail = cn
		else:
			self.tail.next = cn
			cn.pre = self.tail
			self.tail = self.tail.next
		return

	def search(self,key):
		if not self.tmpPointer: self.tmpPointer = self.head
		tmpPointer = self.tmpPointer
		while tmpPointer:
			if tmpPointer.key == key: 
				print ("Found! Key:",key,"Value:",tmpPointer.val)
				self.tmpPointer = tmpPointer
				return
			else: tmpPointer = tmpPointer.next
		tmpPointer = self.tmpPointer
		while tmpPointer:
			if tmpPointer.key == key: 
				print ("Found! Key:",key,"Value:",tmpPointer.val)
				self.tmpPointer = tmpPointer
				return
			else: tmpPointer = tmpPointer.pre
		print ("Not Find! Invalid key.")
		return

	def startwith(self,startstr):
		if not self.tmpPointer: self.tmpPointer = self.head
		num = 0
		tmpPointer = self.tmpPointer
		while tmpPointer:
			if tmpPointer.key.startswith(startstr): 
				print ("Found! Key:",tmpPointer.key,"Value:",tmpPointer.val)
				num += 1
			tmpPointer = tmpPointer.next
		tmpPointer = self.tmpPointer.pre
		while tmpPointer:
			if tmpPointer.key.startswith(startstr): 
				print ("Found! Key:",tmpPointer.key,"Value:",tmpPointer.val)
				num += 1
			tmpPointer = tmpPointer.pre
		if num == 0: print("Not Found")
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
	var = input("Please enter command command:parameter0 parameter1 parameter2:\ne.g.[insert|search|startwith|exit]:[key|startstr] [value]\n")
	t = tire()
	while True:
		if var == 'exit': break
		varlist = var.split(':')
		if len(varlist) > 1:
			if varlist[0] == 'insert' and len(varlist) == 2 and len(varlist[1].split()) == 2: t.insert(varlist[1].split()[0],varlist[1].split()[1])
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


