# write a code to cheak if a given string is a palindrome or not.

def is_palindrome(s):
    s = s.lower()
    s = ''.join(c for c in s if c.isalnum())
    return s == s [::-1]
s = "A man,a plan,a canal-panama"
print(is_palindrome(s))