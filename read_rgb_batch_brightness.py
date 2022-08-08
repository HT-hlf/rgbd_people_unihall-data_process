# coding:utf-8
# @Author     : HT
# @Time       : 2022/1/9 21:05
# @File       : read_depth_fixed.py
# @Software   : PyCharm


import os,glob
import cv2
import numpy as np

def contrast_brightness_demo(image, c, b):            # 定义方法， c @ contrast  对比度 ; b @ brightness 亮度
    h, w, ch = image.shape
    blank = np.zeros([h, w, ch], image.dtype)         # 定义一张空白图像
    dst = cv2.addWeighted(image, c, blank, 1-c, b)     # 设定权重
    return dst
    # cv2.imshow("con-bri-demo", dst)
#
# ————————————————
# 版权声明：本文为CSDN博主「Wupke」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/Kefenggewu_/article/details/108597532



in_dir=r'..\rgbd_people_unihall.tar\rgbd_people_unihall\mensa_seq0_1.1\rgb_jpg'
out_dir = r'..\rgbd_people_unihall.tar\rgbd_people_unihall\mensa_seq0_1.1\rgb_jpg_brightness_0_2'
if not os.path.isdir(out_dir):
    os.makedirs(out_dir)


for files in glob.glob(in_dir + '/*'):
    filepath, filename = os.path.split(files)
    im = cv2.imread(files)
    im_bright=contrast_brightness_demo(im, 0.2, 0)

    new_path = os.path.join(out_dir, filename)
    cv2.imwrite(new_path, im_bright)
    # cv2.imshow('image:', im)
    # cv2.imshow('image_bright:', im_bright)
    # cv2.waitKey(0)