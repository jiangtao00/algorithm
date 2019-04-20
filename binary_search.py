# coding:utf-8

class ValueError(Exception):
	pass
def binary_search(ls, start, end, mid, value):
	""" binary search
	param: 
	ls: is a list, 
	start: just like a curcor that started from the list
	end: the same with start but end with the list\
	value: the item that want to be found
	return: the location of the value 
	"""
	# if the value is not in the list, return None
	if start > end:
		return None
	# if the value's location is start or end, just return
	if value == ls[start]:
		return start
	elif value == ls[end]:
		return end
	# get the value's location
	else:
		if value == ls[mid]:
			return mid
		elif value < ls[mid]:
			return binary_search(ls, start, mid, int((mid-start)/2), value)
		elif value > ls[mid]:
			return binary_search(ls, mid, end, int((mid-start)/2+1+mid), value)
if __name__ == '__main__':
	ls = [1, 2, 3, 4, 5, 6, 7, 8]
	# Use a loop test program to see if it meets the requirements
	try:
		for i in range(1, 9):
			print(binary_search(ls, 0, len(ls)-1, int(len(ls)/2), i))
	except ValueError:
		print("somthing was wrong")