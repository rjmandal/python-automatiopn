str = input("enter any string : ")
C_str = ""
stk =[]
for w in str:
    stk.append(w)
while stk!=[]:
    C_str += stk.pop()

if str == C_str:
    print("palindrome")
else:
    print("not palindrome")