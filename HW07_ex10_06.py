# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def is_sorted(lists):
	for i in range(len(lists) - 1):
		if  lists[i] > lists[i+1]:
			return False

	return True


# print (repr(is_sorted([1,2,3,4,5])))

def main():
	pass

if __name__ == '__main__':
	main()