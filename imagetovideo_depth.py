# coding:utf-8
# @Author     : HT
# @Time       : 2022/1/23 21:46
# @File       : imagetovideo.py
# @Software   : PyCharm

import cv2
import os,glob
import random

img = cv2.imread('seq0_0000_0.jpg')  #读取第一张图片
fps = 25
imgInfo = img.shape
size = (imgInfo[1],imgInfo[0])  #获取图片宽高度信息
print(size)
fourcc = cv2.VideoWriter_fourcc(*"MJPG")
videoWrite = cv2.VideoWriter('camera_three_depth_rgb.mp4',fourcc,fps,size)# 根据图片的大小，创建写入对象 （文件名，支持的编码器，5帧，视频大小（图片大小））
#videoWrite = cv2.VideoWriter('0.mp4',fourcc,fps,(1920,1080))
dir=r'..\rgbd_people_unihall.tar\rgbd_people_unihall\mensa_seq0_1.1\depth_jpg_rgb_camera_three'

# files = os.listdir('VideoData/')
# out_num = len(files)
# for i in range(0,out_num):
#     fileName = 'VideoData/'+str(i)+'.png'    #循环读取所有的图片,假设以数字顺序命名
#     img = cv2.imread(fileName)
#     videoWrite.write(img)# 将图片写入所创建的视频对象
for files in glob.glob(dir + '/*'):
    img = cv2.imread(files)
    videoWrite.write(img)  # 将图片写入所创建的视频对象