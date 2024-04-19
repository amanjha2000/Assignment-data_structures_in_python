# write a code to find the intersection of two given list.

def list_intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(list_intersection(list1, list2))
