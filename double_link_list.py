class Node(object):
	"""docstring for ClassName"""
	def __init__(self, item):
		self.elem = item
		self.next = None
		self.prev = None
class DoubuleLinkList(object):
	def __init__(self, node=None):
		self.__head = node

	def is_empty(self):
		"""judge the list is None or not"""
		return self.__head == None

	def length(self):
		# the length of the list
		# use the cur to travel the list
		cur = self.__head
		# use the count to note the number
		count = 0
		while cur != None:
			count += 1
			cur = cur.next
		return count

	def travel(self):
		# travel the list
		cur = self.__head
		while cur != None:
			print(cur.elem, end=" ") 
			cur = cur.next
		print("")

	def add(self, item):
		# add something from head of the list
		node = Node(item)
		node.next = self.__head
		# self.__head = node
		# node.next.prev = node

		self.__head.prev = node
		self.__head = node 

	def append(self, item):
		# add a node to the end of the list
		node = Node(item)
		# if the list is empty, just make the node be the first
		if self.is_empty():
			self.__head = node
		else:
			# the variable of cur is the cursor, note the data of the list to the end 
			cur = self.__head
			# get the node of end in the list
			while cur.next != None:
				cur = cur.next
			# add the node to the list
			cur.next = node
			node.prev = cur

	def insert(self, pos, item):
		""" add the item in the list by pos
		:param: pos start from 0
		"""
		if pos <= 0:
			self.add(item)
		elif pos > self.length()-1:
			self.append(item)
		else:
			pre = self.__head
			count = 0
			# find the location of list that want to insert
			while count < (pos-1):
				count += 1
				pre = pre.next
			# when the circulation is done, the pre point to the pos
			node = Node(item)

			# node.next = pre.next
			# node.next.prev = node
			# pre.next = node
			# node.prev = pre

			# # other way
			node.next = pre
			node.prev = pre.prev
			pre.prev.next = node
			pre.prev = node

			# # other way
			# node.next = pre
			# node.prev = pre.prev
			# pre.prev = node
			# node.prev.next = node

	def remove(self, item):
		# remove a node
		cur = self.__head
		while cur != None:
			if cur.elem == item:
				# judge the node is head or not
				# if the node is the head node
				if cur == self.__head:
					self.__head = cur.next
					if cur.next:
						# judge the node have the only one node or not
						cur.next.prev = None
				else:
					cur.prev.next = cur.next
					if cur.next:
						cur.next.prev = cur.prev
				break
			else:
				cur = cur.next

	def search(self, item):
		# search the item from the Node
		cur = self.__head
		while cur != None:
			if cur.elem == item:
				return True
			else:
				cur = cur.next
		return False

if __name__ == '__main__':
	dll = DoubuleLinkList()
	print(dll.is_empty())
	print(dll.length())

	dll.append(1)
	print(dll.is_empty())
	print(dll.length())

	dll.append(2)
	dll.add(8)
	dll.append(3)
	dll.append(4)
	dll.append(5)
	dll.append(6)
	dll.travel()
	# 8, 1, 2, 3, 4, 5, 6
	dll.insert(-1, 9)
	dll.travel()
	dll.insert(3, 11)
	dll.insert(9, 20)	# 9 8 1 11 2 3 4 5 6 20
	dll.travel()
	dll.remove(9)
	dll.remove(20)
	dll.travel()
	print(dll.length())