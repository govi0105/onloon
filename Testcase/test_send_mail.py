import pytest
from Page.index_page import IndexPgae
from Page.login_page import LoginPage
from Page.send_mail_page import MailPage
from selenium.webdriver.chrome.options import Options
from selenium. webdriver.chrome.service import Service
import ddt
import time
import unittest
from selenium import webdriver
from TestData.data import Data
import logging



@pytest.mark.mail
@pytest.mark.usefixtures("conftest_env")
@pytest.mark.usefixtures("refresh_page")
class Test_mail():
    # @classmethod
    # def setUpClass(cls):
    #     # #浏览器实例化
    #     # cls.driver=webdriver.Chrome()
    #     # cls.driver.maximize_window()
    #     # 屏蔽浏览器通知
    #     cls.options=webdriver.ChromeOptions()
    #
    #     prefs = {
    #         'profile.default_content_setting_values':
    #             {
    #                 'notifications': 2
    #             }
    #
    #     }
    #     #启动浏览器
    #     cls.options.add_experimental_option('prefs', prefs)
    #     cls.driver = webdriver.Chrome(options=cls.options)
    #
    #
    #
    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()


    @pytest.mark.smoke
    def test_1_login(self,conftest_env):
        logging.basicConfig(level=logging.INFO)

        logging.info("元素已可见。等待元素可见总时长：开始等待的时间，等待结束的时间：")
        #正常登录
        LoginPage(conftest_env).login(username=Data.login_data["username"],passwd=Data.login_data["passwd"])
        #断言
        time.sleep(2)
        assert IndexPgae(conftest_env).isExist_quit()

        # self.driver.get(Data.mail_url)

    @pytest.mark.smoke
    def test_2_mail(self,conftest_env):
        # logging.basicConfig(level=logging.INFO)
        #
        # logging.info("元素已可见。等待元素可见总时长：开始等待的时间，等待结束的时间：")
        # #正常登录
        # LoginPage(self.driver).login(username=Data.login_data["username"],passwd=Data.login_data["passwd"])

        logging.info("开始了")
        logging.info("info输出")
        MailPage(conftest_env).send_mail()

        # self.assertTrue(IndexPgae(self.driver).isExist_quit())
        # self.driver.get(Data.mail_url)


# 执行命令 失败重复2次间隔时间10秒 pytest -m mail --reruns  2  --reruns-delay 10 --html=test_mail.html
#  E:\onloon\Testcase\test_send_mail.py
# pytest E:\onloon\Testcase\test_send_mail.py -m mail --reruns  2  --reruns-delay 10 --html=E:\onloon\Outputs\html\TestReport.html
