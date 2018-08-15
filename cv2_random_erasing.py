import cv2
import random
import math
import numpy as np

class RandomErasing(object):
    
    def __init__(self, probability = 0.9, sl = 0.02, sh = 0.4, r1 = 0.3, mean=[0.914, 0.4822, 0.4465]):
        self.probability = probability
        self.mean = mean
        self.sl = sl
        self.sh = sh
        self.r1 = r1
       
    def __call__(self, img):

        if random.uniform(0, 1) > self.probability:
            return img

        for attempt in range(100):
            sp = img.shape
            print(sp)
            area = sp[0] * sp[1]
       
            target_area = random.uniform(self.sl, self.sh) * area
            aspect_ratio = random.uniform(self.r1, 1/self.r1)

            h = int(round(math.sqrt(target_area * aspect_ratio)))
            w = int(round(math.sqrt(target_area / aspect_ratio)))
            if w < sp[1] and h < sp[0]:
                x1 = random.randint(0, sp[0] - h)
                y1 = random.randint(0, sp[1] - w)
                if len(sp) == 3:
                    img[x1:x1+h, y1:y1+w,0] = self.mean[0]
                    img[x1:x1+h, y1:y1+w,1] = self.mean[1]
                    img[x1:x1+h, y1:y1+w,2] = self.mean[2]
                else:
                    img[x1:x1+h, y1:y1+w] = self.mean[0]
                return img

        return img

if __name__ == "__main__":
     img=cv2.imread("/home/xgx/Downloads/timg.jpeg")
     #img=img-127.5
     #img=img/128.0
     re=RandomErasing(0.99,0.02,0.4,0.3,[125, 40, 213])
     re(img)
     cv2.namedWindow("img",0)
     cv2.imshow("img",img)
     cv2.waitKey()     
