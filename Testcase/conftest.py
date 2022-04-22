# -*- coding: utf-8 -*-
# @Time : 2022/4/18 11:35
# @Author : gw
import pytest
from selenium import webdriver

driver = None
@pytest.fixture(scope="class")
def conftest_env():
    print("===========测试类级别的fixture=======")
    global driver
    #前置条件
    options = webdriver.ChromeOptions()

    prefs = {
        'profile.default_content_setting_values':
            {
                'notifications': 2
            }

    }
    # 启动浏览器
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    #分隔符
    yield driver
    #后置条件
    driver.quit()
@pytest.fixture
def refresh_page():
    print("===========测试类级别的fixture=======")
    global driver

    yield driver
    # 后置条件
    driver.refresh()
