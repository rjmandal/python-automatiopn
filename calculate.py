import os
s = []
top = -1


def IsEmpty():
    if top == -1:
        return True
    else:
        return False


def Push(S, item):
    S.append(item)
    global top
    top += 1


def Pop(S):
    if(IsEmpty()):
        print('stack is empty')
    else:
        a = S.pop()
        global top
        top -= 1
        return a


def peek(S):
    if(IsEmpty()):
        print('stack is empty')
    else:
        return S[top]


def display(S):
    if(IsEmpty()):
        print('stack is empty')
    else:
      print(S[top], '----->top')
      print(S[-1:-(top+2):-1])


while(True):
    os.system('cls')
    display(s)
    print('1.push')
    print('2.pop')
    print('3.peek')
    print('4.Exit')
    ch = int(input('enter your choice : '))
    if(ch == 1):
        item = input('enter the data to push : ')
        Push(s, item)
        input('press any key to continue---')
    elif(ch == 2):
        a=Pop(s)
        print(a)
        input('press any key to continue---')
    elif(ch == 3):
        a = peek(s)
        print('peeked value', a)
        input('press any key to continue---')
    elif(ch == 4):
        break
