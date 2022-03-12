
R ={
    "om" : 76,
    "jai" : 45,
    "bob" : 89,
    "ali" : 65,
    "anu" : 90,
    "tom" : 82
}

stk =[]
def push(S,item):
    S.append(item)

def Pop(S):
    if S==[]:
        return None
    else:
        return S.pop()
    
for name in R:
    if(R[name] > 75):
        push(stk,name)
t = len(stk)
while(t):
   print(stk.pop(),end=" ")
   t-=1
    
