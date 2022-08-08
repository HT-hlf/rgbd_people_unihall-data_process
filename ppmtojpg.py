# coding:utf-8
# @Author     : HT
# @Time       : 2022/1/9 23:06
# @File       : pgmtojpg.py
# @Software   : PyCharm

from PIL import Image
import os, glob
import cv2

def batch_image(in_dir, out_dir):
    if not os.path.exists(out_dir):
        print(out_dir, 'is not existed.')
        os.mkdir(out_dir)

    if not os.path.exists(in_dir):
        print(in_dir, 'is not existed.')
        return -1
    count = 0
    for files in glob.glob(in_dir + '/*'):
        filepath, filename = os.path.split(files)
        print(filename)

        out_file = filename.split('.')[0] + '.jpg'
        # print(filepath,',',filename, ',', out_file)
        im = cv2.imread(files)
        new_path = os.path.join(out_dir, out_file)
        print(count, ',', new_path)
        count = count + 1
        im=cv2.rotate(im, cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imwrite(new_path,im)
        # cv2.imshow('image', im)
        # cv2.waitKey(0)
        # im = Image.open(files)
        # print(im)
        # new_path = os.path.join(out_dir, out_file)
        # print(count, ',', new_path)
        # count = count + 1
        # im.save(os.path.join(out_dir, out_file))


if __name__ == '__main__':
    batch_image(r"..\rgbd_people_unihall.tar\rgbd_people_unihall\mensa_seq0_1.1\rgb", r'..\rgbd_people_unihall.tar\rgbd_people_unihall\mensa_seq0_1.1\rgb_jpg')