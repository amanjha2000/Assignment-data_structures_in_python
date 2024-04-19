# write  a code to marge teo sorted lists into a single list.

def merge_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
print(merge_sorted_lists(list1, list2))
