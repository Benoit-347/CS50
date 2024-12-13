import re

def is_palindrome(text):
    # Remove non-alphanumeric characters and make lowercase
    clean_text = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    # Check if it matches the reverse of itself
    return bool(re.match(rf"({clean_text[:len(clean_text)//2]})(?=\1[::-1])?", clean_text))

print(is_palindrome("Able was I saw Elba")) # True 
