import re
def validate_pin(pin):
    if len(pin) in (4, 6):
        if re.search('[^0-9]', pin) == None:
            return True
    return False

"""
import re
def validate_pin(pin):
    if (len(pin) == 4 or len(pin) == 6) and pin.isdigit() == True:
        return True
    return False
"""