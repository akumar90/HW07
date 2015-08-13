# I want to be able to call cumulative_sum from main w/ various lists and 
# get returned a list of the cumulative sums.
# You are safe to expect only integers in a flat list.
# Ex. the cumulative sum of [1, 2, 3] is [1, 3, 6]
#  - in the above example I want returned the list [1, 3, 6]
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def nested_sum(lists):
	sumOfNumbers = 0
	for i in lists:

		if type(i) is int:
			sumOfNumbers += i

		elif type(i) is list :
			sumOfNumbers += nested_sum(i)

	return sumOfNumbers

def cumulative_sum(lists):

	cumulative_list = []

	for i in range(len(lists)):
		cumulative_list.append(nested_sum(lists[:i+1]))

	print (repr(cumulative_list))

cumulative_sum([1, 2, [[[[3],[[[2]]],[[2]],[1],44]]],[3]])

def main():
	pass

if __name__ == '__main__':
	main()