
from google.colab import drive
import os
import pandas as pd
from matplotlib import pyplot as plt
drive.mount("/content/drive")
os.chdir("/content/drive/MyDrive/data")
import cv2
imagen1 =cv2.imread("1p.png", 0)
imagen2 =cv2.imread("2p.png", 0)
adicion = cv2.addWeighted(imagen1,0.8,imagen2,0.1,0)
plt.imshow(adicion)


imagen1 =cv2.imread("1p.png", 0)
imagen2 =cv2.imread("2p.png", 0)
resta = cv2.subtract(imagen1,imagen2)
plt.imshow(resta)
