
import cv2
import numpy as np
import math

#----------------------------------------------------------------#

#IMAGE READING
image_main = cv2.imread('image.png')

#----------------------------------------------------------------#

#GREY SCALING OF IMAGE
image = np.empty_like(image_main[:, :, 0])
image[:] = 0.299 * image_main[:, :, 0] + 0.587 * image_main[:, :, 1] + 0.114 * image_main[:, :, 2]

cv2.imwrite('gray image.png',image)

#----------------------------------------------------------------#

#Imgae Scaling
resize = np.zeros([int(image.shape[0]/2), int(image.shape[1]/2)])

for i in range(0, resize.shape[0]):
    for j in range(0, resize.shape[1]):
        resize[i,j] = image[i*2, j*2]
        
cv2.imwrite('gray image scaled.png',resize)

#----------------------------------------------------------------#

#Image Translation
resize = np.zeros([image.shape[0], image.shape[1]], int)
for i in range(0, resize.shape[0]):
    for j in range(0, resize.shape[1]):
        if j>=50 and i>=50:
            resize[i,j] = image[i, j]
                   
cv2.imwrite('gray image translated.png',resize)

#----------------------------------------------------------------#

#horizontal axis Flipping
resize = np.zeros([image.shape[0], image.shape[1]], int)

for i in range(0, resize.shape[0]):
    for j in range(0, resize.shape[1]):
        resize[i][j] = image[i][image.shape[1]-1-j]


cv2.imwrite('gray image flip horizontal.png',resize)               

#----------------------------------------------------------------#

#vertical axis Flipping
resize = np.zeros([image.shape[0], image.shape[1]], int)

for i in range(0, resize.shape[0]):
    for j in range(0, resize.shape[1]):
        resize[i][j] = image[image.shape[0]-1-i][j]


cv2.imwrite('gray image flip vertical.png',resize) 

#----------------------------------------------------------------#

#Inverting gray-scale image

resize = np.zeros([image.shape[0], image.shape[1]], int)
for i in range(0, resize.shape[0]):
    for j in range(0, resize.shape[1]):
        resize[i][j] = 255 - image[i][j]


cv2.imwrite('gray image inversion.png',resize) 

#----------------------------------------------------------------#


# ### Rotating the gray-scale image
radian_angle = math.radians(-45)
rotation = np.zeros(image.shape, dtype = int)
(h,w) = image.shape
mid_x,mid_y = (w//2, h//2)

for i in range(h):
    for j in range(w):
        x= round((j-mid_x)*math.cos(radian_angle)-(i-mid_y)*math.sin(radian_angle)+mid_x)
        y= round((j-mid_x)*math.sin(radian_angle)+(i-mid_y)*math.cos(radian_angle)+mid_y)
        if (0 <= x < w) and (0 <= y < h):
            rotation[i,j] = image[y,x]
        
cv2.imwrite('gray image rotated.png',rotation) 

#----------------------------------------------------------------#

#Imgae reading
image1 = cv2.imread('image.png')

#--------------------------------------#
#Imgae Scaling

resize = np.zeros([int(image1.shape[0]/2), int(image1.shape[1]/2),3])

for i in range(0, resize.shape[0]):
    for j in range(0, resize.shape[1]):
        resize[i,j,:] = image1[i*2, j*2,:]
        
cv2.imwrite('image scaled.png',resize)

#--------------------------------------#
#Image Translation

resize = np.zeros([image1.shape[0], image1.shape[1],3], int)

for i in range(0, resize.shape[0]):
    for j in range(0, resize.shape[1]):
        if j>=50 and i>=50:
            resize[i,j,:] = image1[i, j,:]
                   
cv2.imwrite('image translated.png',resize)

#--------------------------------------#
#horizontal axis Flipping

resize = np.zeros([image1.shape[0], image1.shape[1],3], int)

for i in range(0, resize.shape[0]):
    for j in range(0, resize.shape[1]):
        resize[i,j,:] = image1[i,image1.shape[1]-1-j,:]


cv2.imwrite('image flip horizontal.png',resize) 

#--------------------------------------#
#vertical axis Flipping

resize = np.zeros([image1.shape[0], image1.shape[1],3], int)

for i in range(0, resize.shape[0]):
    for j in range(0, resize.shape[1]):
        resize[i,j,:] = image1[image1.shape[0]-1-i,j,:]


cv2.imwrite('image flip vertical.png',resize) 

#----------------------------------------------------------------##----------------------------------------------------------------#







