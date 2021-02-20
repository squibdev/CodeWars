# Elegant Solution
from re import sub
def printer_error(s):
    # uses string.format() on regex to remove any a-m letter, count remaining (errors)
    # returns error count/total count with "{}/{}"
    return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))

# Original Solution
def printer_error(s):
    control = 'abcdefghijklm'
    error_count = 0
    control_count = 0
    total_count = 0
    
    for letter in s:
        if letter in control:
            control_count+=1
        else:
            error_count+=1
            
    total_count = control_count + error_count
    
    return str(error_count) + '/' + str(total_count)