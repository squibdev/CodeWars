import string

def is_pangram(s):
    return set(string.ascii_lowercase) <= set(s.lower())

"""
import string
import re 

def is_pangram(s):
    alphabet = list(string.ascii_lowercase)
    s = re.sub(r'\W+','',s).lower()
    for letter in alphabet:
        count = s.count(letter)
        if count == 0:
            return False
    return True
"""