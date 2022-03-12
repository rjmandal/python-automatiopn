

str = ""
stk = []
infx  = input("enter infix expression : ")
for w in infx:
    a = ord(w)
    if(a==41):
        if(stk!=[]):
            s='0'
            while(ord(s)!=40):
                s=stk.pop()
                if ord(s)!=40:
                    str+=s
                else:
                    break
    elif(a==40 or (a>=42 and a<=47)):
        stk.append(w)
    elif((a>=65 and a<=90) or (a>=97 and a<=122) or(w>='0' and w<='9')):
        str+=chr(a)
    
print(str)
