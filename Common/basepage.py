# -*- coding=utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging
import time



class Base(object):
    def __init__(self,driver):
        #self.driver = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe",service_log_path="D:/test.log")
        self.driver = driver

    #等待元素可见
    def wait_eleVisible(self,locator,timeout=30,poll_frequency=0.5,model_name="model"):
        logging.info("等待元素可见：{}".format(locator))
        try:
            t1=time.time()
            WebDriverWait(self.driver,timeout,poll_frequency).until(EC.visibility_of_element_located(locator))
            # WebDriverWait(self.driver, timeout,poll_frequency).until(EC.presence_of_all_elements_located(((By.XPATH, "//span[@class='nameDetail']"))))
            # WebDriverWait(self.driver, timeout,poll_frequency,model_name).until(EC.visibility_of_element_located(locator),message='元素')
            # 获取结束等待的时间
            t2 = time.time()
            #h获取等待的总时长 - 以秒为单位
            logging.info("元素已可见。等待元素可见总时长：开始等待的时间，等待结束的时间：{0}".format(t2-t1))
        except TimeoutException as msg:
            print("元素不存在",msg)
            raise

    def save_webImg(self,model_name):
        #文件名称=模块名称——当前时间.png
        picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        filePath = ("E:/onloon/Outputs/img/{0}_{1}.png".format(model_name,picture_time))
        try:

            self.driver.get_screenshot_as_file("E:/onloon/Outputs/img/{0}_{1}.png".format(model_name,picture_time))
            logging.info("截图成功，文件路径为：{}".format(filePath))
        except:
            logging.exception("截图失败！！")
            raise


    #查找元素
    def get_element(self,locator,model_name="model"):
        logging.info("查找模块：{}下的元素{}".format(model_name,locator))
        try:
            self.driver.find_element(*locator)
            logging.info("查找元素成功")
        except:
            # 写击日志
            logging.exception("查找元素失败。")
            # 截图
            self.save_webImg(model_name)
            raise


    #点击元素
    def click_element(self,locator,model_name="model"):
        #查找元素
        ele = self.get_element(locator,model_name)
        #元素操作
        logging.info("点击操作：模块 {} 下的元素 {}".format(model_name,locator))
        try:
            ele.click()
        except:
            # 写击日志
            logging.exception("点击元素操作失败")
            # 截图
            self.save_webImg(model_name)
            raise

    #输入内容
    def input_text(self,locator,value,model_name="model"):
        # 查找元素
        ele = self.get_element(locator, model_name)
        # 元素操作
        logging.info("输入操作：模块 {} 下的元素 {} 输入文本 {}".format(model_name, locator,value))
        try:
            ele.send_keys(value)
        except:
            # 写击日志
            logging.exception("元素输入操作失败")
            # 截图
            self.save_webImg(model_name)
            raise

    #获取元素的属性
    def get_element_attribute(self,locator,attr,model_name="model"):
        # 查找元素
        ele = self.get_element(locator, model_name)
        # 元素操作
        logging.info("获取元素的属性：模块 {} 下的元素 {} 的属性 {}".format(model_name, locator, attr))
        try:
            return ele.get_attribute(attr)
        except:
            # 写击日志
            logging.exception("获取元素的属性失败")
            # 截图
            self.save_webImg(model_name)
            raise

    #获取元素的文本内容
    def get_element_text(self,locator,model_name="model"):
        # 查找元素
        ele = self.get_element(locator, model_name)
        # 元素操作
        logging.info("获取元素文本：模块 {} 下的元素 {} ".format(model_name, locator))
        try:
            return ele.text
        except:
            # 写击日志
            logging.exception("获取元素文本失败")
            # 截图
            self.save_webImg(model_name)
            raise

    # 窗口切换。新的窗口，其他窗口
    def switchwindow(self,str="",index = None):
        if str == "new":
            #等待新窗口出现
            time.sleep(2)
            windows=self.driver.window_handles
            #切换到窗口
            self.driver.switch_to.window(windows[-1])
        else:
            #获取所有窗口
            windows = self.driver.window_handles
            if index != None and 0<= int(index) < len(windows):

                self.driver.switch_to.window(windows[int(index)])
                # 切换到index下标所有的窗口。

    #alert切换
    def switch_alert(self,action="accept"):
        #等待alert出现
        WebDriverWait(self. driver, 10). until(EC.alert_is_present())
        #关闭alert弹框-accept, dismiss
        alert = self.driver.switch_to.alert
        if action == "accept":
            alert.accept()   #查阅alert类的accept函数
        else:
            alert.dismiss()  #查阅alert类的dismiss函数

    def switch_iframe(self,action="accept"):
        #等待alert出现
        WebDriverWait(self. driver, 10). until(EC.alert_is_present())
        #关闭alert弹框-accept, dismiss

    # 输入框 - 清空内容


    #上传
    def upload (self):
        pass