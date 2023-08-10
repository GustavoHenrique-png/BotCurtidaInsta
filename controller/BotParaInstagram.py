from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class IgBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(keep_alive=True)
    
    def Login(self):
        driver = self.driver
        driver.get('https://www.instagram.com')
        driver.implicitly_wait(2)

        userElement = driver.find_element("xpath","/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
        userElement.clear()
        userElement.send_keys(self.username)

        passElement = driver.find_element("xpath","/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
        passElement.clear()
        passElement.send_keys(self.password)

        loginButton = driver.find_element("xpath","/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button")
        loginButton.click()

        driver.implicitly_wait(5)

        information = driver.find_element("xpath","/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button")
        information.click()

        driver.implicitly_wait(5)

        notify = driver.find_element("xpath","/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
        notify.click()

        driver.implicitly_wait(5)

        self.Like('memes')
    
    def Like(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(5)
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

leaBot = IgBot('ale26bday','?Snow759')

leaBot.Login()