import numpy as np 
import pandas as pd 
import cv2 
import os 
import glob
import tqdm
from random import shuffle
import pickle
from os.path import basename
path="/home/geekysethi/Desktop/vrinda_project/Dataset/*"
path_image="/home/geekysethi/Desktop/vrinda_project/Dataset"
path_dir=np.sort(glob.glob(path))


# print(path_dir)
all_csv=[]
for i in path_dir:
	
	all_csv.append(glob.glob(str(i)+'/*.csv'))

# print(all_csv)

train_images=[]
labels=[]

demo_path=str(all_csv[0])[2:-2]
print(demo_path)

df= pd.read_csv(demo_path)       
print(df.head())
print(os.path.join(path_image,df.image[0]))
print(basename(os.path.join(path_image,df.image[0]))[0])


for i in range(len(df)):

	print(i)
	image_path=os.path.join(path_image,df.image[i])
	img=cv2.imread(image_path,1)
	img=img[df.top_left_y[i]:df.bottom_right_y[i],df.top_left_x[i]:df.bottom_right_x[i]]
	label=basename(os.path.join(path_image,df.image[0]))[0]

	train_images.append(img)
	labels.append(label)
	# cv2.imshow('frame',img)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()

print(len(train_images))
print(len(labels))


# for j in all_csv:
# 	print(str(j)[2:-2])
# 	df=pd.read_csv(str(j)[2:-2])
# 	print(df.head())
