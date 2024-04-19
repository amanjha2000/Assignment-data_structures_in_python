# write a code to find all occurences of a substring whithin another string.

def find_all_occurrences(s, sub):
    start = 0
    while start < len(s):
        start = s.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)
s = "I love love love my country!"
sub = "love"
print(f"All occurrences of '{sub}' in '{s}' are at indices: {list(find_all_occurrences(s, sub))}")

