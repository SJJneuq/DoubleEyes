# coding:utf-8

from ctypes import *

import os


BASE_DIR = os.path.abspath('.')

# dll 文件路径
DLL_PATH_DoubleEye = os.path.join(BASE_DIR, "DLL", "DoubleEye.dll")
DoubleEye = cdll.LoadLibrary(DLL_PATH_DoubleEye)


rectify_0_path = os.path.join(BASE_DIR, "left_rectify.jpg").replace('\\','\\\\')
rectify_1_path = os.path.join(BASE_DIR, "right_rectify.jpg").replace('\\','\\\\')
out_path = str(BASE_DIR+'\\').replace('\\','\\\\')
print(out_path)
print(rectify_0_path)
print(rectify_1_path)

def test():

	img_l = c_char_p(bytes(rectify_0_path, 'utf-8'))
	img_r = c_char_p(bytes(rectify_1_path, 'utf-8'))
	out = c_char_p(bytes(out_path, 'utf-8'))
	number = c_int(0)
	number = DoubleEye.FourStickman(img_l, img_r, out)
	print(number)

if __name__ == '__main__':
	test()