# write a code to count the number of words in a string.

def count_words(s):
    return len(s.split())
print(count_words(" Hello ,world "))
print(count_words("this is a test"))