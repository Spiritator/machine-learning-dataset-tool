# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 13:31:29 2018

@author: Leo Tsai
"""

import os,csv
import xml.etree.ElementTree as ET

def get_class_name(filename):
    for i in range(len(filename)):
        if filename[i]=='0' or filename[i]=='1' or filename[i]=='2' or filename[i]=='3' or filename[i]=='4' or filename[i]=='5' or filename[i]=='6' or filename[i]=='7' or filename[i]=='8' or filename[i]=='9':
            tail=i
            break
    return filename[0:tail-1]

def get_xml_data(xml_file):
    bndbox_data = ET.parse(xml_file)
    bndbox_data = bndbox_data.getroot()
    
    #bndbox_data.findall('.')
    #for elem in bndbox_data.findall('./filename'):
    #    print(elem.tag, elem.text)  
    #elem=bndbox_data.findall('./filename')
    
    pic_filename=pic_path+bndbox_data.findall('./filename')[0].text
    xmin=bndbox_data.findall('./object/bndbox/xmin')[0].text
    ymin=bndbox_data.findall('./object/bndbox/ymin')[0].text
    xmax=bndbox_data.findall('./object/bndbox/xmax')[0].text
    ymax=bndbox_data.findall('./object/bndbox/ymax')[0].text
    class_name=get_class_name(bndbox_data.findall('./filename')[0].text)
    
    return [pic_filename,{'xmin':xmin,'ymin':ymin,'xmax':xmax,'ymax':ymax,'class_name':class_name}]

xmls_path='oxford_pet/annotations/xmls/'
pic_path='oxford_pet/images/'

directory = os.fsencode(xmls_path)

data_dict={}

for file in os.listdir(directory):
    xml_file_name = os.fsdecode(file)
    if xml_file_name.endswith(".xml"): 
        bndbox_info=get_xml_data(xmls_path+xml_file_name)
        data_dict[bndbox_info[0]]=bndbox_info[1]


with open('oxford_pet_dataset_annotation.csv', 'w', newline='') as csvfile:
                fieldnames=['path','xmin','ymin','xmax','ymax','class_name']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
                for item in data_dict:
                    writer.writerow({'path':item,'xmin':data_dict[item]['xmin'],'ymin':data_dict[item]['ymin'],'xmax':data_dict[item]['xmax'],'ymax':data_dict[item]['ymax'],'class_name':data_dict[item]['class_name']})
        

