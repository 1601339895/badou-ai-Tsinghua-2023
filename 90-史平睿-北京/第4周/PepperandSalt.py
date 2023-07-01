
import cv2 as cv
import numpy as np
from numpy import shape
import random

def fun1(src,percetage):
    NoiseImg=src
    NoiseNum=int(percetage*src.shape[0]*src.shape[1])
    for i in range(NoiseNum):
		#每次取一个随机点
		#把一张图片的像素用行和列表示的话，randX 代表随机生成的行，randY代表随机生成的列
        #random.randint生成随机整数
		#椒盐噪声图片边缘不处理，故-1
        randX=random.randint(0,src.shape[0]-1)
        randY=random.randint(0,src.shape[1]-1)
        #random.random生成随机浮点数，随意收到一个像素点有一半的可能是白点255，一半的可能是黑点0
        if  random.random() <= 0.5:
            NoiseImg[randX, randY] = 0
        else:
            NoiseImg[randX, randY] = 255
    return NoiseImg

img = cv.imread('lenna.png', 0)
img1 = fun1(img,0.3)
#在文件夹中写入命名为lenna_PepperandSalt.png的加噪后的图片
cv.imwrite('lenna_PepperandSalt.png',img1)
cv.imshow("lenna_PepperandSalt", img1)

img = cv.imread('lenna.png')
img2 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("source", img2)
cv.waitKey(0)