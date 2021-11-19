import  pyautogui
pyautogui.hotkey("alt","tab")
pyautogui.sleep(2)
j=1
for i in range(0,8):
    pyautogui.click(x=1031,y=271)
    pyautogui.sleep(1)
    pyautogui.click(x=766,y=496)
    pyautogui.click(x=766,y=496)
    pyautogui.sleep(2)
    pyautogui.hotkey("win","alt","r")
    pyautogui.click(x=1838,y=1039)
    pyautogui.sleep(1)
    pyautogui.click(x=1825,y=883)
    pyautogui.sleep(2)
    pyautogui.click(x=957,y=522)
    # if j==1:
    #     pyautogui.sleep(60*53)
    #     pyautogui.sleep(22)
    #     pyautogui.sleep(30)
    if j==1:
        pyautogui.sleep(60*60)
        pyautogui.sleep(16)
        pyautogui.sleep(30)
    elif j==2:
        pyautogui.sleep(60*57)
        pyautogui.sleep(12)
        pyautogui.sleep(30)
    elif j==3:
        pyautogui.sleep(60*51)
        pyautogui.sleep(20)
        pyautogui.sleep(30)
    elif j==4:
        pyautogui.sleep(60*54)
        pyautogui.sleep(23)
        pyautogui.sleep(30)
    elif j==5:
        pyautogui.sleep(60*50)
        pyautogui.sleep(13)
        pyautogui.sleep(30)
    elif j==6:
        pyautogui.sleep(60*53)
        pyautogui.sleep(26)
        pyautogui.sleep(30)
    elif j==7:
        pyautogui.sleep(60*43)
        pyautogui.sleep(18)
        pyautogui.sleep(30)
    elif j==8:
        pyautogui.sleep(60*50)
        pyautogui.sleep(16)
        pyautogui.sleep(30)
    j+=1
    pyautogui.hotkey("win","alt","r")
    pyautogui.sleep(2)
    pyautogui.hotkey("ctrl","tab")