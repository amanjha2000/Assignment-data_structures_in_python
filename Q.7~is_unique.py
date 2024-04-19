# write a code to determine if a string has all unique character.

def is_unique(s):
    return len(s) == len(set(s))
print(is_unique("world")) 
