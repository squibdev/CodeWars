def is_isogram(string):
    return len(string) == len(set(string.lower()))

"""
def is_isogram(string):
    output = False
    if string == "":
        output = True
    for _ in string.lower():
        if string.lower().count(_) == 1:
            output = True
        else:
            output = False
            break
            
    return output
"""