#devlop a code that prompts the user to input two set of strings .then , 
# print the elements that are presents in tha first set but not in the second set


set1 = set(input("Please enter the elements of the first set, separated by spaces: ").split())
set2 = set(input("Please enter the elements of the second set, separated by spaces: ").split())

difference = set1 - set2


print("The elements that are in the first set but not in the second set are: ", difference)
