# develop a code that prompts the user to input two sets of strings.
# Then print the symmentric diference of these two sets.


set1 = set(input("Please enter the strings for the first set separated by space: ").split())
set2 = set(input("Please enter the strings for the second set separated by space: ").split())


sym_diff_set = set1.symmetric_difference(set2)


print("The symmetric difference of the two sets is: ", sym_diff_set)
