# write a code to reverse a list in place without using any build-in reverse function.

def reverse_list(lst):
    start_index = 0
    end_index = len(lst) -1
    while start_index < end_index:
        lst [start_index],lst [end_index] = lst [end_index],lst [start_index]
        start_index += 1
        end_index -= 1
        return lst


my_list = [1,2,3,4,5]
print(reverse_list(my_list))