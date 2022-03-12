import  pyautogui
pyautogui.hotkey("alt","tab")
pyautogui.sleep(2)
j=3
for i in range(0,13):
    pyautogui.click(x=1031,y=271)
    pyautogui.sleep(1)
    pyautogui.click(x=766,y=496)
    # pyautogui.sleep(2)
    pyautogui.click(x=766,y=496)
    pyautogui.sleep(2)
    pyautogui.hotkey("win","alt","r")
    pyautogui.moveTo(1838,1039)
    # pyautogui.click(x=1838,y=1039)
    pyautogui.sleep(1)
    pyautogui.click(x=1819,y=889)
    pyautogui.sleep(2)
    pyautogui.click(x=957,y=522)
    # if j==1:
    #     pyautogui.sleep(60*49)
    #     pyautogui.sleep(23)
    #     pyautogui.sleep(30)
    if j==3:
        pyautogui.sleep(60*52)
        pyautogui.sleep(24)
        pyautogui.sleep(30)
    elif j==4:
        pyautogui.sleep(60*49)
        pyautogui.sleep(14)
        pyautogui.sleep(30)
    elif j==5:
        pyautogui.sleep(60*48)
        pyautogui.sleep(26)
        pyautogui.sleep(30)
    elif j==6:
        pyautogui.sleep(60*58)
        pyautogui.sleep(1)
        pyautogui.sleep(30)
    # if j==6:
    #     pyautogui.sleep(60*50)
    #     pyautogui.sleep(13)
    #     pyautogui.sleep(30)
    elif j==7:
        pyautogui.sleep(60*48)
        pyautogui.sleep(20)
        pyautogui.sleep(30)
    elif j==8:
        pyautogui.sleep(60*50)
        pyautogui.sleep(21)
        pyautogui.sleep(30)
    elif j==9:
        pyautogui.sleep(60*43)
        pyautogui.sleep(27)
        pyautogui.sleep(30)
    elif j==10:
        pyautogui.sleep(60*32)
        pyautogui.sleep(10)
        pyautogui.sleep(30)
    elif j==11:
        pyautogui.sleep(60*30)
        pyautogui.sleep(15)
        pyautogui.sleep(30)
    elif j==12:
        pyautogui.sleep(60*43)
        pyautogui.sleep(6)
        pyautogui.sleep(30)
    elif j==13:
        pyautogui.sleep(60*37)
        pyautogui.sleep(6)
        pyautogui.sleep(30)
    elif j==14:
        pyautogui.sleep(60*29)
        pyautogui.sleep(10)
        pyautogui.sleep(30)
    elif j==15:
        pyautogui.sleep(60*41)
        pyautogui.sleep(14)
        pyautogui.sleep(30)
    elif j==16:
        pyautogui.sleep(60*30)
        pyautogui.sleep(16)
        pyautogui.sleep(30)
    elif j==17:
        pyautogui.sleep(60*41)
        pyautogui.sleep(4)
        pyautogui.sleep(30)
    elif j==18:
        pyautogui.sleep(60*38)
        pyautogui.sleep(10)
        pyautogui.sleep(30)
    elif j==19:
        pyautogui.sleep(60*50)
        pyautogui.sleep(6)
        pyautogui.sleep(30)
    elif j==20:
        pyautogui.sleep(60*42)
        pyautogui.sleep(10)
        pyautogui.sleep(30)
    # elif j==21:
    #     pyautogui.sleep(60*48)
    #     pyautogui.sleep(23)
    #     pyautogui.sleep(30)
    # elif j==22:
    #     pyautogui.sleep(60*42)
    #     pyautogui.sleep(3)
    #     pyautogui.sleep(30)
    # elif j==23:
    #     pyautogui.sleep(60*48)
    #     pyautogui.sleep(5)
    #     pyautogui.sleep(30)
    # elif j==24:
    #     pyautogui.sleep(60*60)
    #     pyautogui.sleep(10)
    #     pyautogui.sleep(30)
    # elif j==25:
    #     pyautogui.sleep(60*45)
    #     pyautogui.sleep(14)
    #     pyautogui.sleep(30)
    # elif j==26:
    #     pyautogui.sleep(60*55)
    #     pyautogui.sleep(18)
    #     pyautogui.sleep(30)
    # elif j==27:
    #     pyautogui.sleep(60*48)
    #     pyautogui.sleep(26)
    #     pyautogui.sleep(30)

    # elif j==28:
    #     pyautogui.sleep(60*44)
    #     pyautogui.sleep(15)
    #     pyautogui.sleep(30)
    # elif j==29:
    #     pyautogui.sleep(60*47)
    #     pyautogui.sleep(10)
    #     pyautogui.sleep(30)
    # elif j==30:
    #     pyautogui.sleep(60*35)
    #     pyautogui.sleep(12)
    #     pyautogui.sleep(30)
    # elif j==31:
    #     pyautogui.sleep(60*52)
    #     pyautogui.sleep(5)
    #     pyautogui.sleep(30)
    # elif j==32:
    #     pyautogui.sleep(60*46)
    #     pyautogui.sleep(18)
    #     pyautogui.sleep(30)
    # elif j==33:
    #     pyautogui.sleep(60*51)
    #     pyautogui.sleep(6)
    #     pyautogui.sleep(30)
    # elif j==34:
    #     pyautogui.sleep(60*43)
    #     pyautogui.sleep(12)
    #     pyautogui.sleep(30)
   
    j+=1
    pyautogui.hotkey("win","alt","r")
    pyautogui.sleep(2)
    pyautogui.hotkey("ctrl","tab")