# For taking screen shots
import pyautogui
import time

# for i in range(10):
#     name="sfdf"+str(i)
#     print(name)
def snapshot():
    for i in range(4):
        myScreenshot = pyautogui.screenshot()
        path=r"C:\Users\HP\Desktop\\" + str(i)+ ".png"
        myScreenshot.save(path)
        time.sleep(30)
