import cv2 
import numpy as np
from matplotlib import pyplot as plt
import urllib.request
import requests as req

img_src = "https://scontent-tpe1-1.xx.fbcdn.net/v/t1.0-9/11214290_979728228728313_6464220580933024886_n.jpg?_nc_cat=105&_nc_eui2=AeExGUqRxcZU4upTetprXJyv_Op4AKU9Oi0KerZLpKGeJ1eNelyKE8Va-EMuyfLeMAnEZ1jPtl2Q3kfCGkqxbtXdZlUhJaJEKiF-E1SavOs0xQ&_nc_ohc=k0ZZmaA6kdEAQkCfmXYSTOBPC0T1JsPb1y8boEcDjKwqiECZRTPWLAivA&_nc_ht=scontent-tpe1-1.xx&oh=f1bcf4ad88a887d8ffa735ea151bdeec&oe=5E3F278B"
resp = urllib.request.urlopen(img_src)
img = np.asarray(bytearray(resp.read()), dtype="uint8")
img = cv2.imdecode(img, cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([gray],[0],None,[256],[0,256])
colors = np.where(hist>5000)
img_number = 0
for color in colors[0]:
    print(color)
    split_image = img.copy()
    split_image[np.where(gray != color)] = 255
    cv2.imwrite("layer_"+str(img_number)+".bmp",split_image)
    img_number+=1
plt.hist(gray.ravel(),256,[0,256])
plt.savefig('plt')
plt.show()