from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class IgBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(keep_alive=True)
    
    def login(self):
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

        driver.implicitly_wait(10)

leaBot = IgBot('ale26bday','?Snow759')

leaBot.login()