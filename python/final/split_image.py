import cv2 
import numpy as np
from matplotlib import pyplot as plt
import requests as req
from PIL import Image,ImageDraw,ImageFont

def Image_split(data):
    global img_src1
    img_src1 = data  
    response1 = req.get(img_src1)
    img = Image.open(BytesIO(response1.content))

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