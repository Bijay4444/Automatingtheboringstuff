import pyautogui

#size of the screen
print(pyautogui.size())
#current coordinates of the mouse cursour
pyautogui.position()

# #moves the cursor to the top left corner
# pyautogui.moveTo(10, 10, duration= 2)

# #moves the cursor relative 
# pyautogui.moveRel(200, 0, duration= 2)

#clicking 
pyautogui.click(375, 9)
pyautogui.doubleClick()
pyautogui.rightClick()
pyautogui.leftClick()
 