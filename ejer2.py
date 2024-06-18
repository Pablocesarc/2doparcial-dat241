from google.colab import drive
import os
import pandas as pd
drive.mount("/content/drive")
os.chdir("/content/drive/MyDrive/data")
import scipy.sparse as sp
imagen1=cv2.imread("1p.png")
imagen2=cv2.imread("2p.png")
m_sparce2=sp.coo_matrix(imagen2[:,:,1])
print(m_sparce2)
