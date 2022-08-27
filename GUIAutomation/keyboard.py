import pyautogui 

#types instantly
pyautogui.click(100,100); pyautogui.typewriter('Hellow world! ')

#for shift arrow like keys
pyautogui.click(100, 100); pyautogui.typewrite(['a', 'b', 'left', 'X', 'Y'], interval=1)

#list of string names of keyboard keys
pyautogui.KEYBOARD_KEYS

#single key pressing
pyautogui.press('F1')

pyautogui.hotkey('ctrl', '0') #it will control O shortcut of editor
