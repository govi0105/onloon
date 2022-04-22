from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from TestData.data import Data
from Common.basepage import Base
import logging
import time
class MailPage:
    # @classmethod
    def __init__(self,driver):
        #self.driver = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe",service_log_path="D:/test.log")
        self.driver = driver


        print("开始输入地址")
        self.driver.get(Data.mail_url)
        print("已输入地址")
        self.driver.refresh()
        time.sleep(1)
        #首页入口
    # def addressee_mail(self):
    #     self.driver.find_element(By.ID, "reviverInp").send_keys(Data.emaildata())


    def send_mail(self):
        #url: https://ydt.onloon.net/#/mail/list

        print("开始发邮箱")
        logging.debug("开始发邮箱")

        loc = (By.XPATH, "//div[@class='mail-slidebar']/button")
        # loc1 ="//div[@class='mail-slidebar']/button"
        # Base.wait_eleVisible(locator=loc1,timeout=30,poll_frequency=0.5,model_name="邮箱发送按钮")

        try:
            WebDriverWait(self.driver,30).until(EC.presence_of_all_elements_located(loc))
            logging.info("元素已可见。等待元素可见总时长：开始等待的时间，等待结束的时间：")
        except TimeoutException as msg:
            print("元素不存在", msg)
        # Base.click_element(locator="//div[@class='mail-slidebar']/button",model_name="点击邮件按钮")
        self.driver.find_element(By.XPATH, "//div[@class='mail-slidebar']/button").click()


        print("收件人：{0}".format(Data.emmail))
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.ID, "reviverInp")))
            logging.info("元素已可见。等待元素可见总时长：开始等待的时间，等待结束的时间：")
        except TimeoutException as msg:
            print("元素不存在", msg)
            raise

        # 输入框 - 清空内容
        self.driver.find_element(By.ID, "reviverInp").clear()
        self.driver.find_element(By.ID, "reviverInp").send_keys(Data.emmail)
        print("主题：{0}".format(Data.themetext))
        self.driver.find_element(By.ID, "jsThemeChar").send_keys(Data.themetext)

        #切换text
        print("开始切换frame")
        time.sleep(1)
        #self.driver.switch_to.frame("vue-tinymce-1649482434077_ifr")
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH,"//iframe[@title='编辑区. 按Alt+0键打开帮助']"))
        print("切换frame成功")
        self.driver.find_element(By.ID, "tinymce").send_keys(Data.mail_text)
        time.sleep(1)
        print("退出frame")
        self.driver.switch_to.default_content()
        print("退出frame成功")
        logging.debug("退出frame成功")
        #点击发送text()="文本值"   //div[@class='sign-chose']//span[text()='发送']
        loc_send="//div[@class='sign-chose']//span[text()='发送']"
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc_send))
        # print(self.driver.find_element(By.XPATH, loc_send))
        self.driver.find_element(By.XPATH, loc_send).click()
        time.sleep(1)
        logging.debug("邮件发送成功")






