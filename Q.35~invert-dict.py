# write a code that inverts a dictionary,swapping keys and values.
# ensure that the inverted dictionary correctly handles cases where multiple keys have the same value by storing 
# the keys as a list in the inverted dictionary.


def invert_dict(input_dict):
    
    inverted_dict = {}


    for key, value in input_dict.items():
        
        if value in inverted_dict:
            inverted_dict[value].append(key)
        
        else:
            inverted_dict[value] = [key]

    
    return inverted_dict


input_dict = {"a": 1, "b": 2, "c": 2, "d": 3}
print(invert_dict(input_dict))
