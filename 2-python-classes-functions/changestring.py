def changeString(st):
    s=list(st)
    vowels=['a','e','i','o','u']
    for i in range(0,len(st)):
        if s[i]=='Z':
            s[i]='a'
        elif s[i]=='z':
            s[i]='A'
        else:
            s[i]=chr(ord(s[i])+1)
        if s[i] in vowels:
            s[i]=s[i].upper()
    return "".join(s)
str1=str(input("Enter string: "))
print("Result:",changeString(str1))
