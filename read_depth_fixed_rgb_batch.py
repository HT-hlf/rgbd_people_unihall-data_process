# coding:utf-8
# @Author     : HT
# @Time       : 2022/1/9 21:05
# @File       : read_depth_fixed.py
# @Software   : PyCharm


import os,glob
import cv2






in_dir=r'..\rgbd_people_unihall.tar\rgbd_people_unihall\mensa_seq0_1.1\depth_jpg'
out_dir = r'..\rgbd_people_unihall.tar\rgbd_people_unihall\mensa_seq0_1.1\depth_jpg_rgb'
if not os.path.isdir(out_dir):
    os.makedirs(out_dir)


for files in glob.glob(in_dir + '/*'):
    filepath, filename = os.path.split(files)
    im = cv2.imread(files)
    im = cv2.applyColorMap(cv2.convertScaleAbs(im, alpha=1), 9)
    new_path = os.path.join(out_dir, filename)
    cv2.imwrite(new_path, im)
    # cv2.imshow('image:', im)
    # cv2.waitKey(0)