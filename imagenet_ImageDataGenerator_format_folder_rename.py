# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 16:54:46 2018

@author: Yung-Yu Tsai

imagenet validation set folder management script
put the raw image into label named folder for keras ImageDataGenerator
"""

import os, sys

dir = ''

class_mapping=dict()

with open(dir+'../imagenet_class_mapping.txt','r') as file_class_mapping:
    for line in file_class_mapping:
        line_content=line.split()
        class_mapping[int(line_content[1])]=line_content[2]
    #class_mapping=ast.literal_eval(class_mapping_file.read())
    

ground_truth=list()

with open(dir+'../ILSVRC2012_validation_ground_truth.txt','r') as file_ground_truth:
    for line in file_ground_truth:
        ground_truth.append(int(line))
        
        
pic_file_list=os.listdir(dir+'../ILSVRC2012_img_val')

#count=0
#for key in class_mapping.keys():
#    os.system('mkdir imagenet_val_imagedatagenerator\%s' % class_mapping[key])
#    count=count+1
#    print('foleder created %d/%d'%(count,1000))
#    
#count=0
#for i in range(len(ground_truth)):
#    os.system('copy ILSVRC2012_img_val\%s imagenet_val_imagedatagenerator\%s' % (pic_file_list[i],class_mapping[ground_truth[i]]))
#    count=count+1
#    print('picture copied %d/%d'%(count,50000))


#%%
# rename folder
    
class_folder_list=os.listdir(dir+'../imagenet_val_imagedatagenerator')
count=0
for key in class_mapping.keys():
    os.system('rename %s %s' % (class_mapping[key],str(key)+'_'+class_mapping[key]))
    count=count+1
    print('foleder renameed %d/%d'%(count,1000))
    
