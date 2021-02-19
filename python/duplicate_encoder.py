def duplicate_encode(word):
    return "".join(["(" if word.lower().count(_) == 1 else ")" for _ in word.lower()])

"""
def duplicate_encode(word):
    output = ""
    word = word.lower()
    for _ in word:
        count = word.count(_)
        if count > 1:
            output += ')'
        else:
            output += '('
    
    return output
"""