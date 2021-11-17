import  pyautogui
pyautogui.hotkey("alt","tab")
pyautogui.sleep(2)
j=1
for i in range(0,2):
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
    if j==1:
        pyautogui.sleep(60*30)
        pyautogui.sleep(30)
        pyautogui.sleep(30)
    elif j==2:
        pyautogui.sleep(60*30)
        pyautogui.sleep(30)
        pyautogui.sleep(30)
    j+=1
    pyautogui.hotkey("win","alt","r")
    pyautogui.sleep(2)
    pyautogui.hotkey("ctrl","tab")