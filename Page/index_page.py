import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from TestData.data import  Data
from selenium. webdriver.chrome.service import Service
class IndexPgae(object):
    def __init__(self, driver):
        # self.driver = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe",service_log_path="D:/test.log")
        self.driver = driver

    def isExist_quit(self):

        try:
            # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(By.XPATH, "//span[@class='nameDetail']"))

            #self.driver.find_element(By.XPATH,"//span[@class='nameDetail']")
            WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(((By.XPATH,"//span[@class='nameDetail']"))))
            return True
        except:
            return False