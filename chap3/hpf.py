import cv2
import numpy as np
from scipy import ndimage
# 定义一个3x3的核
kernel_3x3 = np.array(
    [[-1, -1, -1],
     [-1,8,-1],
     [-1,-1,-1]])

# 定义一个5x5的核
kernel_5x5 = np.array(
    [[-1, -1, -1, -1, -1],
     [-1, 1, 2, 1, -1],
     [-1, 2, 4, 2, -1],
     [-1, 1, 2, 1, -1],
     [-1, -1, -1, -1, -1]])

# 将读入的图像转换为灰度格式
img = cv2.imread("../images/p3.jpg", 0)

# 使用scipy ndimage的convolve函数实现卷积
k3 = ndimage.convolve(img, kernel_3x3)
k5 = ndimage.convolve(img, kernel_5x5)

blurred = cv2.GaussianBlur(img, (11,11), 0)
g_hpf = img - blurred

cv2.imshow("3x3", k3)
cv2.imshow("5x5", k5)
cv2.imshow("g_hpf", g_hpf)
cv2.waitKey(0)
cv2.destroyWindow()