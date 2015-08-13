# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
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

# print (nested_sum([1, 2, [[[[3],[[[2]]],[[2]],[1],44]]],[3]]))

def main():
	pass


if __name__ == '__main__':
	main()