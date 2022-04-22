# -*- coding: utf-8 -*-
# @Time : 2022/4/21 16:06
# @Author : gw
import os, zipfile,time

#打包目录为zip文件(未压缩)

def make_zip(source_dir, output_filename):

    zipf = zipfile.ZipFile(output_filename, 'w')

    pre_len = len(os.path.dirname(source_dir))

    for parent, dirnames, filenames in os.walk(source_dir):

        for filename in filenames:

            pathfile = os.path.join(parent, filename)

            arcname = pathfile[pre_len:].strip(os.path.sep) #相对路径


            zipf.write(pathfile, arcname)

    zipf.close()
if __name__ == '__main__':
    theme_time = time.strftime("%Y-%m-%d-%H-%M", time.localtime(time.time()))
    make_zip(source_dir=r"/Outputs/html", output_filename='测试报告{}.zip'.format(theme_time))
