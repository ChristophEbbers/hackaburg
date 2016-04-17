
# coding: utf-8

# In[45]:

get_ipython().magic(u'matplotlib inline')
import cv2
from matplotlib import pyplot as plt
image = cv2.imread('blue.jpg')
plt.imshow(image)


# In[67]:

rbg = cv2.split(image)
hsvimage = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
hsv = cv2.split(hsvimage)
newR = (-(rbg[0]-rbg[1])/(rbg[0]+rbg[1]))+150
print newR
hsvimage = cv2.merge([newR, rbg[1], rbg[2]])
plt.imshow(hsvimage)
cv2.imwrite('converted.jpg', hsvimage)

