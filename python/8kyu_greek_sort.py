def greek_comparator(lhs, rhs):
    # the tuple greek_alphabet is defined in the global namespace
    return greek_alphabet.index(lhs) - greek_alphabet.index(rhs)

"""
def greek_comparator(lhs, rhs):
    for item in greek_alphabet:
        if lhs == rhs:
            return 0
            break
        if item == lhs:
            return -1
            break
        if item == rhs:
            return 1
"""