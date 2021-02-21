def is_palindrome(text):
    if text:
        return text[0] == text[-1] and is_palindrome(text[1:-1])
    return True
