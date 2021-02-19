import string

def duplicate_count(text):
    a = string.ascii_lowercase + '0123456789'
    c = 0
    for _ in a:
        if text.lower().count(_) > 1:
            c +=1
    return c