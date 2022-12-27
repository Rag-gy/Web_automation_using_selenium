import os   # the os module is used to apply the path of the website to all the necessary areas
import time # we use the time module to provide a delay in certain areas
import random
from selenium import webdriver  # the web driver module is used to make automation and access the website to be automated through get request
from selenium.webdriver.common.by import By     # the By module is used to specify the category of the element selection
from selenium.webdriver.common.keys import Keys     # the keys module is used to insert keyboard keys and text
from selenium.webdriver.common.action_chains import ActionChains    # the ActionChains is used to execute certain actions on the web which will be seen later

def reset_pass(driver):     # this function is callled if we forget or enter wrong password
    driver.find_element(By.LINK_TEXT, "Forgot password?").click()     # this is used to find an element by tracking a text in the <a> tag i.e. (link tag)

    driver.implicitly_wait(30)  # we use this implicity_wait here instead of time.sleep() because this will make the program wait eventhough the loading is done before but not in the case of implicitly_wait

    text = driver.find_element(By.ID, "modalusername")  # in this we use the find element by ID (html id given to that element) to find an element which is present in the webpage and has the given id

    sel = ActionChains(driver)  # we select the driver on which we perform the actions

    sel.move_to_element(text).click().perform()     # we use this to move the cursor in the element position and perform click 


def scrollslow(y_val, driver, delay):   # we perform the scrolling of the webpage using this function and we recieve the delay between scrolls and the y axis distance to get to the required position
    for i in range(0, y_val+50, 8):     # we give 8 steps where because single step result in very slow scrolling
        driver.execute_script(f"window.scrollTo(0, {i})")   # the 0 indicate the x axis and the {i} indicate the y axis
        time.sleep(delay)       # we give the delay here for a slower scroll


os.environ['PATH'] += "E:\Programming\python\Selenium\msedgedriver.exe"     # we've used this because there will be a chance when we have to enter the path of the edge driver many times and so we just define that where ever they ask a path we will enter this path using the os module

driver = webdriver.Edge()   # we use the webdriver of microsoft edge here

driver.get("https://www.w3schools.com/")    # we perform automation in the given website which we access using the get request

driver.maximize_window()    # this function is used to maximize the window size

driver.implicitly_wait(10)  

mailid = "nonom34064@cadolls.com"   # the current mail id to be entered
pword = "Ambulimama417@"            # the pass key

login = driver.find_element(By.ID, "w3loginbtn")    # we select the login button    
login.click()   # we perform the click on the login button  

id = driver.find_element(By.ID, "modalusername")    # we select the email input field
id.send_keys(mailid)    # the send_keys is used to send the mail ID in the field

pas = driver.find_element(By.ID, "current-password")
pas.send_keys(pword)  #Ambulimama417@

driver.implicitly_wait(10)

signup = driver.find_element(By.CLASS_NAME, "Button_button__URNp\+")    # the By.CLASS_NAME is used to select the first element which has the given class name
signup.click()  # we initiate sign in 
try:

    err = driver.find_element(By.CLASS_NAME, "Alert_iwrp__5q1xH")   # here we try to check if we get an alert message for wrong data 
    if err.is_displayed():  # if we get an alert message then we try to continue without signing in
        if err.text == "Make sure you type your email and password correctly. Both your password and email are case-sensitive.":
            reset_pass(driver)
        elif err.text == "A user with this email does not exist":
            print("Un registered user")
            exit()


except:
    driver.find_element(By.XPATH, '//a[@href="https://w3schools.com"]').click() # now we go to the home page by using xpath which is used to select the elements based on their properties

    driver.implicitly_wait(30)

    search = driver.find_element(By.ID, "search2")  # we search for the course

    search.send_keys("python", Keys.ENTER)  # we search for the python course and then press enter

    driver.find_element(By.LINK_TEXT, "Start learning Python now »").click()    # we now select the start learning Python option

    scrollslow(1000, driver, 0.02)  # we will then scroll down and find the elements accordingly
    
    driver.find_element(By.XPATH, "//a[@href='python_getstarted.asp']").click()     # we will got to the next page and scroll further

    scrollslow(3000, driver, 0.025)

    lesson = [" Variables", " Data Types", " Numbers", " Castings", " Strings", " Booleans", " Operators", " Lists", " Tuples", " Sets", " Dictionaries", " If...Else", " While Loops", " For Loops", " Functions", " Lambda", " Arrays", " Classes/Objects", " Inheritance", " Iterators", " Scope", " Modules"," Dates", " Math"]     # we've entered the sections in the python  course to select from

    study = lesson[random.randrange(0, len(lesson)-1)]  # we randomly select the value from among them

    driver.find_element(By.LINK_TEXT, "Python"+study).click()   # we will then select the options accordingly

    if study != " Operators":
        driver.find_element(By.LINK_TEXT, "Try it Yourself »").click()  # we will select the try yourself option
    
    else:
        driver.find_element(By.LINK_TEXT, "Run example »").click()

    driver.find_element(By.ID, "runbtn").click()    # then we will run the program to see the results

