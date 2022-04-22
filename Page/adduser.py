# -*- coding=utf-8 -*-
from selenium import webdriver
import time
from common.base import Base
import time


class AddUser(Base):

    def add_user(self, user, phone, password, repassword):
        """登录后添加用户"""
        yonghu = ('id', 'uname')
        self.send(yonghu, user)
        shouji = ('id', 'uphone')
        self.send(shouji, phone)
        mima = ('id', 'password')
        self.send(mima, password)
        remima = ('id', 'password2')
        self.send(remima, repassword)
        time.sleep(1)
        button = ('id', 'savebtn2')
        self.click(button)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    url = ""
    driver.get(url)