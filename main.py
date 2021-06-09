def front_back(s):
    length = len(s)
    s = list(s)
    temp = s[0]
    s[0] = s[length - 1]
    s[length - 1] = temp
    s = ''.join(s)
    return s
print (front_back("ba"))
