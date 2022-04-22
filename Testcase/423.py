#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import zipfile
import time
def get_zip_file(input_path, result):
  """
  对目录进行深度优先遍历
  :param input_path:
  :param result:
  :return:
  """
  files = os.listdir(input_path)
  for file in files:
    if os.path.isdir(input_path + '/' + file):
      get_zip_file(input_path + '/' + file, result)
    else:
      result.append(input_path + '/' + file)
def zip_file_path(input_path, output_path, output_name):
  """
  压缩文件
  :param input_path: 压缩的文件夹路径
  :param output_path: 解压（输出）的路径
  :param output_name: 压缩包名称
  :return:
  """
  f = zipfile.ZipFile(output_path + '/' + output_name, 'w', zipfile.ZIP_DEFLATED)
  filelists = []

  get_zip_file(input_path, filelists)

  for file in filelists:
    f.write(file)
  # 调用了close方法才会保证完成压缩
  print(filelists)
  f.close()
  # return output_path + r"/" + output_name
  return  r"/" + output_name


if __name__ == '__main__':
  theme_time = time.strftime("%Y-%m-%d-%H", time.localtime(time.time()))
  zip_file_path(input_path=r"E:/onloon/Outputs/", output_path='E:/onloon/Outputs/', output_name= '测试报告{}.zip'.format(theme_time))
