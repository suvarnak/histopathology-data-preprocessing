import numpy as np
import tifffile as tifi
import imageio

import os
os.environ["CV_IO_MAX_IMAGE_PIXELS"] = pow(2,40).__str__()

import cv2 
import glob

FILE_EXT = "tif"
PROC_FILE_EXT = "png"

def get_crops(img_name,save_path):
    img = tifi.imread(img_name)
    tiff_file_name =  os.path.split(img_name)[1]
    tiff_file_name =  tiff_file_name.split(sep=".")[0]
    y=0
    x=0
    h=255
    w=256
    count = 0 
    max_x = (int) (img.shape[0]/256)
    max_y = (int) (img.shape[1]/256)
    for i in range(max_y):
        crop_image = img[x:x+w, y:y+h]
        #print(crop_image.shape)
        #cv2.imwrite(os.path.join(save_path,str(tiff_file_name+"crop_h"+str(count)+".tiff")),crop_image)	  
        x=0
        for i in range(max_x):
            crop_image = img[x:x+w, y:y+h]
            cv2.imwrite(os.path.join(save_path,str(tiff_file_name+"crop_v"+str(count)+"."+ PROC_FILE_EXT)),crop_image)	  
            x = x + 256
            #print(x,y,h,w)
            count = count+1
        y = y + 256
        #print(x,y,h,w)
        count = count+1

def create_crops_dataset(file_list,class_name):
    train_img_count = (int)(len(file_list)*0.7) # change to 0.8 if you want 80-20 for train-test split
    for tiff_file in file_list:
        if train_img_count >= 0:
            save_path = os.path.join(proc_train_test_dataset_dir,"train",class_name)
        else: 
            save_path = os.path.join(proc_train_test_dataset_dir,"test",class_name)
        cropped_img_list = get_crops(tiff_file,save_path)
        train_img_count = train_img_count - 1

def process_files(filelist,class_name):
		for tiff_file in file_list:
				print("image file name {}".format(tiff_file))
				W = 1024
				oriimg = tifi.imread(tiff_file)
				height, width, d= oriimg.shape
				imgScale = W/width
				newX,newY = oriimg.shape[1]*imgScale, oriimg.shape[0]*imgScale
				newimg =  cv2.resize(oriimg,(int(newX),int(newY)))
				bgr_img = newimg
				b,g,r = cv2.split(bgr_img)
				rgb_img = cv2.merge([r,g,b])
				print(os.path.split(tiff_file))
				tiff_file_name =  os.path.split(tiff_file)[1]
				print(os.path.join(proc_dataset_dir,tiff_file_name))
				cv2.imwrite(os.path.join(proc_dataset_dir,class_name,tiff_file_name),rgb_img)

dataset_root_dir = "./data"
proc_dataset_dir = "./data_small"

classes = os.listdir(dataset_root_dir)
print(classes)



if os.path.exists(proc_dataset_dir)  :
	  print("data alread processed once!")
else:
    os.makedirs(proc_dataset_dir)

for class_name in classes:
    if not os.path.exists(os.path.join(proc_dataset_dir,class_name))  :
        os.makedirs(os.path.join(proc_dataset_dir,class_name))	
    img_path = os.path.join(dataset_root_dir,class_name,"*."+FILE_EXT)
    #print("@@@@@@@@@@@@@@@",img_path)
    file_list = glob.glob(img_path)
    #print(file_list)
    process_files(file_list,class_name)

proc_train_test_dataset_dir = "./processed_data"
if not os.path.exists(proc_train_test_dataset_dir)  :
    os.makedirs(proc_train_test_dataset_dir)	
for class_name in classes:
    if not os.path.exists(os.path.join(proc_train_test_dataset_dir,"train",class_name))  :
        os.makedirs(os.path.join(proc_train_test_dataset_dir,"train",class_name))	
    if not os.path.exists(os.path.join(proc_train_test_dataset_dir,"test",class_name))  :
        os.makedirs(os.path.join(proc_train_test_dataset_dir,"test",class_name))	
    downsized_img_path = os.path.join(proc_dataset_dir,class_name,"*."+FILE_EXT)
    #print("@@@@@@@@@@@@@@@",img_path)
    file_list = glob.glob(downsized_img_path)
    create_crops_dataset(file_list,class_name)