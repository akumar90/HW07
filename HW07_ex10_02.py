# I want to be able to call capitalize_nested from main w/ various lists 
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def capitalize_nested(lists):
	capitalized_list = []

	for i in lists:

		if type(i) is str:
			capitalized_list.append(i.upper())

		elif type(i) is list :
			capitalized_list.append(capitalize_nested(i))

	return capitalized_list

# print (capitalize_nested(['a', 'b', [[[['cfd'],[[['dedd']]],[['eewdwd']],['eedsdd'],'ffwvw']]],['efvdw']]))

def main():
	pass

if __name__ == '__main__':
	main()