def is_palindrome(word: str):
    """Return True if word is a palindrome, False if not."""
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and is_palindrome(word[1:-1])

#word[::-1] is reverse string

print(is_palindrome('12521'))
print(is_palindrome('abba'))
print(is_palindrome('ababa'))
print(is_palindrome('abbot'))
