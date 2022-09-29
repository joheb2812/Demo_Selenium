import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:

    textbox_username_Xpath = '//input[@id="Email"]'
    textbox_password_Xpath = '//input[@id="Password"]'
    button_login_Xpath = '//button[text() = "Log in"]'
    link_logout_Xpath = '//a[text() = "Logout"]'


    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_Xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_Xpath).send_keys(username)
        time.sleep(2)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_Xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_Xpath).send_keys(password)
        time.sleep(2)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_Xpath).click()
        time.sleep(2)

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.link_logout_Xpath).click()
        time.sleep(2)