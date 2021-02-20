def add_binary(a,b):
    c = a + b
    output = ''
    
    while c >= 1:
        if c % 2 == 1:
            output += '1'
        if c % 2 == 0:
            output += '0'
        
        c //= 2
        
    return output[::-1]