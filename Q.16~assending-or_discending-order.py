# write a code to cheak if a given list is sorted (either in assending or discanding order) or not.

def is_sorted(lst):
    return lst == sorted(lst) or lst == sorted(lst , reverse = True)
my_list1 = [1,2,3,4,5]
my_list2 = [5,4,3,2,1]
my_list3 = [1,3,2,4,5]
print(is_sorted(my_list1))
print(is_sorted(my_list2))
print(is_sorted(my_list3))