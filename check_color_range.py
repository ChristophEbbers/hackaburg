
# coding: utf-8

# In[4]:

get_ipython().magic(u'matplotlib inline')
import cv2
from matplotlib import pyplot as plt
image = cv2.imread('blue.jpg')
plt.imshow(image)


# In[6]:

rbg = cv2.split(image)
hsvimage = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
hsv = cv2.split(hsvimage)
newR = (-(rbg[0]-rbg[2])/(rbg[0]+rbg[2]))

count = 0
for i in range(0, len(newR)):
    for j in range(0, len(newR)):
        if (newR[i][j] < 42 or newR[i][j] > 44) and hsv[1][i][j] > 96 and hsv[2][i][j] < 98:
            count += 1
            
height, width, channels = image.shape
threshold = 0,2 * width * height
if count > threshold: 
    print('Tot')
else:
    print('alles gut {}'.format(count))
hsvimage = cv2.merge([newR, hsv[1]+100, hsv[2]+100])
plt.imshow(hsvimage)
cv2.imwrite('converted2.jpg', hsvimage)

