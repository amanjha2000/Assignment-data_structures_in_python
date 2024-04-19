# write acode that prompts the user to input two sets of characters.Then, prints the union of this two sets.

set1 = set(input("please enter the character for the first set :"))
set2 = set(input("please enter the charcater for the second set : "))

union_set = set1.union(set2)
print("the union of two sets is:",union_set)