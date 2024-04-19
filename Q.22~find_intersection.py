# create a code that prompts the user to enter two aets of intergers separates by commas.
# then ,print the intersetion f two sets.

def find_intersection():
    set1 = set(map(int,input("Enter the first set of integers separted by commas :").split(',')))
    set2 = set(map(int,input("Enter the second set of integer separted by commas :").split(',')))
    intersection = set1 & set2
    print(f"the intersection of the two sets in :{intersection}")

find_intersection()