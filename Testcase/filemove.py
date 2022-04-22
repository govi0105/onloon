# -*- coding: utf-8 -*-
# @Time : 2022/4/21 16:26
# @Author : gw
import os
import shutil

pwd = os.getcwd()
fpath = os.path.join(pwd, "dian")
target = os.path.join(pwd, "电子书")

c = 0
for i in os.listdir(fpath):
    d = os.path.join(fpath, i)
    if (os.path.isdir(d)):
        for j in os.listdir(d):
            f = os.path.join(d, j)
            trail = j.split(".")[-1]
            if (trail == "pdf"):
                shutil.move(f, target)
                c += 1

print("移动{}次".format(c))