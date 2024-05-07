def is_palindrome(x):
    if x < 0:
        return False
    else:
        x = str(x)
        return x == x[::-1]
print(is_palindrome(10))