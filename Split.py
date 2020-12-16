def splitAtUpperCase(s):
    for i in range(len(s)-1)[::-1]:
        if s[i].isupper() and s[i+1].islower():
            s = s[:i]+' '+s[i:]
        if s[i].isupper() and s[i-1].islower():
            s = s[:i]+' '+s[i:]
    return s.split()

b = (splitAtUpperCase('TheLongAndWindingRoad')) 

a = ' '
NewSentence = a.join(b)
print (NewSentence)

