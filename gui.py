import pyautogui,time
import csv
inputfile = csv.reader(open('contact.csv','r'))
time.sleep(5)
pyautogui.click(1191,623)
time.sleep(2)
ctr=0;
for row in inputfile:
    if ctr !=0:
        name = row[0]
        no=row[1]
        pyautogui.click(11168,122)
        time.sleep(2)
        pyautogui.click(695,280)
        pyautogui.typewrite(name, interval=0.25) 
        pyautogui.click(711,343)
        pyautogui.typewrite(name, interval=0.25) 
        pyautogui.click(1215,121)
        time.sleep(5) 
        pyautogui.press('esc')
        time.sleep(5)
    else: 
        ctr=1 