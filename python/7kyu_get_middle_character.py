def get_middle_v2(s):
    return s[(len(s)-1)//2:len(s)//2+1]

def get_middle_v1(s):
    print(len(s))
    #return s[len(s)/2:(len(s)/2)-1] if len(s) % 2 == 0 else s[len(s)/2]
    
    if len(s) % 2 == 0:
        return s[int(len(s)/2 - 1):int(len(s)/2 + 1)]
    else:
        return s[int((len(s) - 1) / 2)]