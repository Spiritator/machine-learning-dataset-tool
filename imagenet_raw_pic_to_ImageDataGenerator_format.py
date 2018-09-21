# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 16:54:46 2018

@author: Yung-Yu Tsai

imagenet validation set folder management script
put the raw image into label named folder for keras ImageDataGenerator
"""

import os, sys, ast
import numpy as np

num_pic_per_class=2

if num_pic_per_class>50 or num_pic_per_class<1 or not isinstance(num_pic_per_class,int):
    raise ValueError('number of picture per class must be integer and between 1 ~ 50')

dir = ''

class_mapping=dict()

with open(dir+'imagenet_class_mapping.txt','r') as file_class_mapping:
    for line in file_class_mapping:
        line_content=line.split()
        class_mapping[line_content[1]]=[line_content[0],line_content[2]]
    
    
with open(dir+'imagenet_class_index.json','r') as file_class_index:
    imagenet_class_index=ast.literal_eval(file_class_index.read())
    
index_convert=dict()
for key in imagenet_class_index.keys():
    index_convert[imagenet_class_index[key][0]]=[key,imagenet_class_index[key][1]]

ground_truth=list()

with open(dir+'ILSVRC2012_validation_ground_truth.txt','r') as file_ground_truth:
    for line in file_ground_truth:
        ground_truth.append(int(line))
        
        
pic_file_list=os.listdir(dir+'ILSVRC2012_img_val')

num_pic_per_class_count=np.zeros(1000)

#%%

count=0
for key in imagenet_class_index.keys():
    os.system('mkdir imagenet_val_imagedatagenerator_setsize_%d\%03d%s' % (num_pic_per_class,int(key),'_'+imagenet_class_index[key][1]))
    count=count+1
    print('foleder renameed %d/%d'%(count,1000))

#count=0
#for key in class_mapping.keys():
#    os.system('mkdir imagenet_val_imagedatagenerator\%s' % str(key)+'_'+class_mapping[key])
#    count=count+1
#    print('foleder created %d/%d'%(count,1000))
#    
    
pic_set_size=1000*num_pic_per_class
count=0
for i in range(len(ground_truth)):
    if num_pic_per_class_count[ground_truth[i]-1]<num_pic_per_class:
        os.system('copy ILSVRC2012_img_val\%s imagenet_val_imagedatagenerator_setsize_%d\%03d%s' % (pic_file_list[i],num_pic_per_class,int(index_convert[class_mapping[str(ground_truth[i])][0]][0]),'_'+index_convert[class_mapping[str(ground_truth[i])][0]][1]))
        num_pic_per_class_count[ground_truth[i]-1]=num_pic_per_class_count[ground_truth[i]-1]+1
        count=count+1
        print('picture copied %d/%d'%(count,pic_set_size))
    if count>pic_set_size:
        break


    
