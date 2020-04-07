import numpy as np
import cv2
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

image = cv2.imread("./test_img.png")

print(image.shape)
