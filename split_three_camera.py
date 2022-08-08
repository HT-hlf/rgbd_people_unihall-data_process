# coding:utf-8
# @Author     : HT
# @Time       : 2022/1/23 21:25
# @File       : split_three_camera.py.py
# @Software   : PyCharm

import os,glob
import shutil
import cv2
import numpy as np

def makedir(dir):
    if not os.path.isdir(dir):
        os.makedirs(dir)

in_dir=r'..\rgbd_people_unihall.tar\rgbd_people_unihall\mensa_seq0_1.1\rgb_jpg'
one_dir=r'..\rgbd_people_unihall.tar\rgbd_people_unihall\mensa_seq0_1.1\rgb_jpg_camera_one'
two_dir=r'..\rgbd_people_unihall.tar\rgbd_people_unihall\mensa_seq0_1.1\rgb_jpg_camera_two'
three_dir=r'..\rgbd_people_unihall.tar\rgbd_people_unihall\mensa_seq0_1.1\rgb_jpg_camera_three'
makedir(one_dir)
makedir(two_dir)
makedir(three_dir)

for files in glob.glob(in_dir + '/*'):
    filepath, filename = os.path.split(files)
    if int(filename.rstrip('.jpg').split('_')[-1])==0:
        # print(0)
        shutil.copy(files,os.path.join(one_dir,filename))
    elif int(filename.rstrip('.jpg').split('_')[-1])==1:
        # print(1)
        shutil.copy(files, os.path.join(two_dir, filename))
    elif int(filename.rstrip('.jpg').split('_')[-1]) == 2:
        # print(2)
        shutil.copy(files, os.path.join(three_dir, filename))
    else:
        pass