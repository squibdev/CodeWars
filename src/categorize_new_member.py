def open_or_senior(data):
    return ["Senior" if (i[0]>=55 and i[1]>7) else "Open" for i in data]

"""
def open_or_senior(data):
    output = []
    for i in data:
        age, hand = i[0], i[1]
        if age >= 55 and hand > 7:
            output.append("Senior")
        else:
            output.append("Open")
        
    return output
"""