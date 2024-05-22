import pyautogui
import pyperclip
from time import sleep
import webbrowser

'''
Creating the first inputs
 Inputs for the user:
 1. User
 2. Password
 3. Which page will be checked
 4. What to comment, in case it wasn't liked yet.
 '''

pyautogui.alert(text='Initializing the program...',timeout=1000)
user = pyautogui.prompt(text='Tell us your Instagram user, please:',title='Mandatory info (1)')
password = pyautogui.password(text='Tell us your password for this user, please:',title='Mandatory info (2)',mask='*')
page = pyautogui.prompt(text='Which user will be checked?',title='Mandatory info (3)')
comment = pyautogui.prompt(text='What do you want to comment, in case it wasnt liked yet?',title='Mandatory info (4)')

def format_text(text):
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl','v')

 #1. Enter instagram website
webbrowser.open('https://www.instagram.com/accounts/login/')
sleep(5)
 #2. Log in with the user account
#pyautogui.screenshot('username.png',region=(1272,352,(1507-1272),(371-352)))
username_field = pyautogui.locateCenterOnScreen('username.png')
pyautogui.click(username_field[0],username_field[1],duration=2)
format_text(user)
sleep(3)

#pyautogui.screenshot('pw.png',region=(1268,406,(1338-1268),(424-406)))
password_field = pyautogui.locateCenterOnScreen('pw.png')
pyautogui.click(password_field[0],password_field[1],duration=2)
format_text(password)
sleep(3)

#Click on login
#pyautogui.screenshot('login.png',region=(1398,466,(1457-1398),(488-466)))
login_bt = pyautogui.locateCenterOnScreen('login.png')
pyautogui.click(login_bt[0],login_bt[1],duration=2)
sleep(8)

#Closing the x on the 'Remember password?' window if it shows

try:
    #pyautogui.screenshot('x.png',region=(1762,126,(1784-1762),(149-126)))
    x = pyautogui.locateCenterOnScreen('x.png')
    pyautogui.click(x[0],x[1],duration=2)
except:
    print("Not found!")

 #3. Search for the user we will check
#pyautogui.screenshot('search.png',region=(985,363,(1024-985),(400-363)))
search = pyautogui.locateCenterOnScreen('search.png')
pyautogui.click(search[0],search[1],duration=2)

#pyautogui.screenshot('search_field.png',region=(1086,280,(1156-1086),(300-280)))
search_field = pyautogui.locateCenterOnScreen('search_field.png')
pyautogui.click(search_field[0],search_field[1],duration=2)
format_text(page)

try:
    #pyautogui.screenshot('no_result.png',region=(1227,657,(1372-1227),(685-657)))
    no_result = pyautogui.locateCenterOnScreen('no_result.png')
    pyautogui.moveTo(1890,26,duration=2)
    pyautogui.click()
    pyautogui.alert(text='User not found!')
except:
    #pyautogui.screenshot('x_search.png',region=(1483,279,(1511-1483),(303-279)))
    x_search = pyautogui.locateCenterOnScreen('x_search.png')
    pyautogui.moveTo(x=x_search[0],y = x_search[1],duration=2)
    pyautogui.move(0,70,duration=1)
    pyautogui.click()
    sleep(5)

 #4. Check for the newest post
#pyautogui.screenshot('posts.png',region=(1235,511,(1318-1235),(534-511)))
posts = pyautogui.locateCenterOnScreen('posts.png')
pyautogui.moveTo(x=posts[0],y=posts[1],duration=2)
pyautogui.move(-50,150,duration=1)
pyautogui.click()
sleep(5)

#pyautogui.screenshot('balloon.png',region=(1380,689,(1419-1380),(726-689)))
balloon = pyautogui.locateCenterOnScreen('balloon.png')
pyautogui.moveTo(balloon[0],balloon[1],duration=1)
pyautogui.move(-50,0,duration=2)

try:  #5. Check if this post was liked already
    #pyautogui.screenshot('liked.png',region=(1329,688,(1365-1329),(724-688)))
    pyautogui.locateCenterOnScreen('liked.png')
    pyautogui.alert(text='Already liked last post!')
    #logout
    #pyautogui.screenshot('close_ig.png',region=(1847,168,(1878-1847),(198-168)))
except: #6. If it wasn't liked, it must like it and comment on it
    sleep(2)
    pyautogui.click()
    sleep(3)
    #pyautogui.screenshot('add.png',region=(1380,821,(1525-1380),(847-821)))
    add = pyautogui.locateCenterOnScreen('add.png')
    pyautogui.click(add[0],add[1],duration=2)
    format_text(comment)
    #pyautogui.screenshot('post_comment.png',region=(1762,824,(1802-1762),(843-824)))
    post_comment = pyautogui.locateCenterOnScreen('post_comment.png')
    pyautogui.click(post_comment[0],post_comment[1],duration=1)
    sleep(3)
    #logout

close_ig = pyautogui.locateCenterOnScreen('close_ig.png')
pyautogui.moveTo(close_ig[0],close_ig[1],duration=2)
pyautogui.click()
sleep(1)
#pyautogui.screenshot('options.png',region=(988,943,(1021-988),(976-943)))
options = pyautogui.locateCenterOnScreen('options.png')
pyautogui.moveTo(options[0],options[1],duration=2)
pyautogui.click()
sleep(2)
pyautogui.screenshot('logout.png',region=(1063,859,(1192-1063),(880-859)))
logout = pyautogui.locateCenterOnScreen('logout.png')
pyautogui.moveTo(logout[0],logout[1],duration=1)
pyautogui.move(0,100,duration=2)
pyautogui.click()
sleep(3)
#close window
pyautogui.moveTo(1890,26,duration=2)
pyautogui.click()

#notify
pyautogui.alert(text='PROCESS COMPLETE!')
