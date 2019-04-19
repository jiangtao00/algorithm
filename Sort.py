class algorithm_sort(object):
	"""this class is all sorted algorithm"""
	# ls is a list parameter
	def __init__(self, ls):
		self.ls = ls

	def bubble_sort(self, ls):
		"""
		this is the bubble sorted, and it is compare with next index from the list
		param: list
		return: list (but sorted)
		"""
		# the i can contral the times of the cycle, and the last value is the biggest by once loop
		for i in range(len(ls)):
			# the compare's times is controled by j 
			for j in range(len(ls)-i-1):
				if ls[j] > ls[j+1]:
					ls[j], ls[j+1] = ls[j+1], ls[j]
		print(ls)
		return ls

	def insert_sort(self, ls):
		"""
		param: get a list from ls
		return: sorted list
		"""
		# get the list's length
		n = len(ls)
		for i in range(n):
			# beacuse the started location is the end of list before sorted
			j = i
			while j>0:
				if ls[j-1] > ls[j]:
					ls[j], ls[j-1] = ls[j-1], ls[j]
				else:
					# print(ls)
					break
				j -= 1
		print(ls)
		return ls

	def select_sort(self, ls):
		"""
		param: a list but not sorted
		return: list but sorted
		"""
		for i in range(len(ls)-1):
			# beacuse the j is started from that sorted by i loops
			for j in range(i, len(ls)-1):
				# set a index note the min value of the index in list that not sorted
				min_index = i
				if ls[j] < ls[min_index]:
					ls[j], ls[min_index] = ls[min_index], ls[j]
		return ls

	def shell_sort(self, ls):
		"""
		param: a list but not sorted
		return: a list with sorted
		"""
		# get the length of the list
		n = len(ls)
		# set the step for started
		step = n // 3
		# we can sort the list until step=1
		while step > 0:
			for i in range(step, n):
				j = i
				while j > 0:
					if ls[j] < ls[j-step]:
						ls[j], ls[j-step] = ls[j-step], ls[j]
						# j -= 1
					else:
						break
					j -= 1
			step //= 2
		print(ls)
		return ls

	def quick_sort(self, ls, start, end):
		"""
		param: list
		return: list (but sorted)
		"""
		# judge the unsatisflied condition of if as recursive exit, just like return somthing.
		if start < end:
			# create two pointers to get the list value 
			low, high = start, end
			# the first value is assumed to be the value that needs to be sorted
			mid_value = ls[0]
			# Break out of the loop when i equals j
			while low < high:
				while low < high and ls[high] > mid_value:
					# let the cursor j move to left once space
					high -= 1
				ls[high] = ls[low]
				while low < high and ls[low] < mid_value:
					low += 1
				ls[low] = ls[high]
			print(ls)
			# quick_sort is recursively called through mid_value into left and right subroutines 
				
			self.quick_sort(ls, start, low-1)
			self.quick_sort(ls, high+1, end)
		return ls
		

if __name__ == '__main__':
	ls = [4, 3, 5, 2, 6, 1, 7]
	al = algorithm_sort(ls)
	al.shell_sort(ls)
	al.bubble_sort(ls)
	al.insert_sort(ls)
	al.quick_sort(ls, 0, len(ls)-1)
