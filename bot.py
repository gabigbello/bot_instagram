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
 #2. Log in with the user account
username_field = pyautogui.locateCenterOnScreen('username.png')
pyautogui.click(username_field[0],username_field[1],duration=2)
sleep(1)
format_text(user)
sleep(2)

password_field = pyautogui.locateCenterOnScreen('pw.png')
pyautogui.click(password_field[0],password_field[1],duration=2)
sleep(1)
format_text(password)
sleep(2)

#Click on login
login_bt = pyautogui.locateCenterOnScreen('login.png')
pyautogui.click(login_bt[0],login_bt[1],duration=2)
sleep(5)

#Closing the x on the 'Remember password?' window if it shows

try:
    x = pyautogui.locateCenterOnScreen('x.png')
    pyautogui.click(x[0],x[1],duration=2)
    sleep(2)
except:
    print("Not found!")
    sleep(2)

 #3. Search for the user we will check
search = pyautogui.locateCenterOnScreen('search.png')
pyautogui.click(search[0],search[1],duration=2)

search_field = pyautogui.locateCenterOnScreen('search_field.png'))
pyautogui.click(search_field[0],search_field[1],duration=2)
format_text(page)

try:
    no_result = pyautogui.locateCenterOnScreen('no_result.png')
    pyautogui.moveTo(1890,26,duration=2)
    pyautogui.click()
    pyautogui.alert(text='User not found!')
except:
    x_search = pyautogui.locateCenterOnScreen('x_search.png')
    pyautogui.moveTo(x=x_search[0],y = x_search[1],duration=2)
    pyautogui.move(0,70,duration=1)
    pyautogui.click()

 #4. Check for the newest post
posts = pyautogui.locateCenterOnScreen('posts.png')
pyautogui.moveTo(x=posts[0],y=posts[1],duration=2)
pyautogui.move(-50,150,duration=1)
pyautogui.click()

balloon = pyautogui.locateCenterOnScreen('balloon.png')
pyautogui.moveTo(balloon[0],balloon[1],duration=1)
pyautogui.move(-50,0,duration=2)

try:  #5. Check if this post was liked already
    pyautogui.locateCenterOnScreen('liked.png')
    pyautogui.alert(text='Already liked last post!')
    pyautogui.moveTo(1890,26,duration=2)
    pyautogui.click()
except: #6. If it wasn't liked, it must like it and comment on it
    pyautogui.click()
    sleep(2)
    add = pyautogui.locateCenterOnScreen('add.png')
    pyautogui.click(add[0],add[1],duration=2)
    format_text(comment)
    post_comment = pyautogui.locateCenterOnScreen('post_comment.png')
    pyautogui.click(post_comment[0],post_comment[1],duration=1)
    sleep(3)
    pyautogui.moveTo(1890,26,duration=2)
    pyautogui.click()    
    pyautogui.alert(text='Last post commented and liked!')

    
 