from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://ydt.onloon.net/")
driver.maximize_window()


# 登录输入账号
driver.find_element('xpath','//input[@placeholder="手机/邮箱"]').send_keys("15039413934")
# 登录输入密码
driver.find_element('xpath','//input[@placeholder="请输入密码"]').send_keys("hhx123")
# 登录确认
driver.find_element('xpath','//button[@type="button"]').click()
time.sleep(3)
# 进入网站轮播图页面X按钮
print(driver.find_element(By.XPATH,"//i[@class='icon-font close-icon']"))
driver.find_element(By.XPATH,"//i[@class='icon-font close-icon']").click()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/div[1]/div[3]/span[4]').click()
time.sleep(10)
# driver.execute_script("arguments[0].click()","//span[@title='邮件']//span[@class='iconfont-new iconEmail']")


# driver.find_element_by_xpath("//span[@title='邮件']//span[@class='iconfont-new iconEmail']").click()
# 进入网站进入轮播图详情
# search=driver.find_element_by_xpath("//div[@class='el-carousel__item is-active is-animating' and contains(@style,'transform')]")
# search.click()
driver.quit()

