# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 16:54:46 2018

@author: Yung-Yu Tsai

imagenet validation set folder management script
put the raw image into label named folder for keras ImageDataGenerator
"""

import os, sys, ast

dir = ''

class_mapping=dict()

with open(dir+'../imagenet_class_mapping.txt','r') as file_class_mapping:
    for line in file_class_mapping:
        line_content=line.split()
        class_mapping[line_content[1]]=[line_content[0],line_content[2]]
    #class_mapping=ast.literal_eval(class_mapping_file.read())
    
with open(dir+'../imagenet_class_index.json','r') as file_class_index:
    imagenet_class_index=ast.literal_eval(file_class_index.read())
    
index_convert=dict()
for key in imagenet_class_index.keys():
    index_convert[imagenet_class_index[key][0]]=[key,imagenet_class_index[key][1]]

ground_truth=list()

with open(dir+'../ILSVRC2012_validation_ground_truth.txt','r') as file_ground_truth:
    for line in file_ground_truth:
        ground_truth.append(int(line))
        
        
pic_file_list=os.listdir(dir+'../ILSVRC2012_img_val')


#%%
# rename folder
    
class_folder_list=os.listdir(dir+'../imagenet_val_imagedatagenerator')
count=0
for key in class_mapping.keys():
    os.system('rename %s %03d%s' % (index_convert[class_mapping[key][0]][0]+'_'+index_convert[class_mapping[key][0]][1],int(index_convert[class_mapping[key][0]][0]),'_'+index_convert[class_mapping[key][0]][1]))
    count=count+1
    print('foleder renameed %d/%d'%(count,1000))
    
