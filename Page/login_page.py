# -*- coding=utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from TestData.data import Data
from selenium. webdriver.chrome.service import Service
class LoginPage:
    # @classmethod
    def __init__(self,driver):
        #self.driver = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe",service_log_path="D:/test.log")
        self.driver = driver
        self.driver.get(Data.login_url)


    #登录功能x
    def login(self,username,passwd):

        loc = (By.XPATH,"//input[@placeholder='手机/邮箱']")
        model_name = "登录页面"
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc))
        # BasePage.wait_eleVisible(*loc,model_name=model_name)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@placeholder='手机/邮箱']").send_keys(username)
        self.driver.find_element(By.XPATH,"//input[@placeholder='请输入密码']").send_keys(passwd)
        self.driver.find_element(By.XPATH,"//button[@type='button']").click()
        time.sleep(2)
        print(self.driver.find_element(By.XPATH, "//i[@class='icon-font close-icon']"))
        self.driver.find_element(By.XPATH, "//i[@class='icon-font close-icon']").click()

        # try:
        #     # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(By.XPATH, "//span[@class='nameDetail']"))
        #
        #     #self.driver.find_element(By.XPATH,"//span[@class='nameDetail']")
        #     WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(((By.XPATH,"//span[@class='nameDetail']"))))
        #     return True
        # except:
        #     return False
    #  # 获取错误提示---没有密码
    # def get_errorMsg_from_loginArea(self):
    #     WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'padding')]")))
    #     return  self.driver.find_element_by_xpath("//div[contains(@class,'padding')]").text
    #
    #
    # #获取错误提示---没有密码
    # def test_get_errorMsg_noPasswd(self):
    #
    #     pass
