# write a code to count the number of vowels in a string.

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum (1 for char in s if char in vowels)
s = "hello world"
print(count_vowels(s))