# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 13:31:29 2018

@author: Leo Tsai
"""

import os
import xml.etree.ElementTree as ET

def get_class_name(filename):
    for i in range(len(filename)):
        if filename[i]=='0' or filename[i]=='1' or filename[i]=='2' or filename[i]=='3' or filename[i]=='4' or filename[i]=='5' or filename[i]=='6' or filename[i]=='7' or filename[i]=='8' or filename[i]=='9':
            tail=i
            break
    return filename[0:tail-1]

def make_xml_data(xml_file,mod_xmls_path):
    bndbox_data = ET.ElementTree(file=xml_file)
    bndbox_data_root = bndbox_data.getroot()
    
    #bndbox_data.findall('.')
    #for elem in bndbox_data.findall('./filename'):
    #    print(elem.tag, elem.text)  
    #elem=bndbox_data.findall('./filename')
    class_name=get_class_name(bndbox_data_root.findall('./filename')[0].text)

    bndbox_data_root.findall('./object/name')[0].text=class_name

    bndbox_data.write(mod_xmls_path+bndbox_data_root.findall('./filename')[0].text[:-4]+'.xml')

xmls_path='oxford_pet/annotations/xmls/'
mod_xmls_path='oxford_pet/annotations/mod_xmls/'

directory = os.fsencode(xmls_path)


for file in os.listdir(directory):
    xml_file_name = os.fsdecode(file)
    if xml_file_name.endswith(".xml"): 
        bndbox_info=make_xml_data(xmls_path+xml_file_name,mod_xmls_path)        

