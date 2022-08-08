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


one_dir=r'..\rgbd_people_unihall.tar\rgbd_people_unihall\mensa_seq0_1.1\depth_jpg_camera_one'
two_dir=r'..\rgbd_people_unihall.tar\rgbd_people_unihall\mensa_seq0_1.1\depth_jpg_camera_two'
three_dir=r'..\rgbd_people_unihall.tar\rgbd_people_unihall\mensa_seq0_1.1\depth_jpg_camera_three'
one_dir_r=r'..\rgbd_people_unihall.tar\rgbd_people_unihall\mensa_seq0_1.1\depth_jpg_camera_one_reduce_num'
two_dir_r=r'..\rgbd_people_unihall.tar\rgbd_people_unihall\mensa_seq0_1.1\depth_jpg__camera_two_reduce_num'
three_dir_r=r'..\rgbd_people_unihall.tar\rgbd_people_unihall\mensa_seq0_1.1\depth_jpg_camera_three_reduce_num'
makedir(one_dir_r)
makedir(two_dir_r)
makedir(three_dir_r)
for in_dir,out_dir in [(one_dir,one_dir_r),(two_dir,two_dir_r),(three_dir,three_dir_r)]:
    count=0
    for files in glob.glob(in_dir + '/*'):
        filepath, filename = os.path.split(files)
        if count%10==0:
            # print(0)
            print(filename)
            shutil.copy(files,os.path.join(out_dir,filename))
        else:
            pass
        count+=1