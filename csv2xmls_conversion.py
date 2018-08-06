# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 14:24:46 2018

@author: Leo Tsai
"""

import os,csv,sys,cv2
import xml.etree.cElementTree as ET
import numpy as np

tmp = []
CLASS_LIST = ["/m/01g317","/m/0ftb8"] # person: "/m/01g317", sunflower: "/m/0ftb8"

def write_xml_file(tmp,folder,filename,path,width,height,depth,obj_name,truncated,occluded,xmin,xmax,ymin,ymax):
    if filename==tmp:
        tree = ET.ElementTree(file="./annotation/"+filename+".xml")
        root = tree.getroot()
        obj = ET.SubElement(root, "object")
        ET.SubElement(obj, "name").text = obj_name
        ET.SubElement(obj, "pose").text = "Unknown"
        ET.SubElement(obj, "truncated").text = truncated
        ET.SubElement(obj, "difficult").text = '0'
        ET.SubElement(obj, "occuluded").text = occluded
        bndbox = ET.SubElement(obj, "bndbox")
        ET.SubElement(bndbox, "xmin").text = str(xmin)
        ET.SubElement(bndbox, "xmax").text = str(xmax)
        ET.SubElement(bndbox, "ymin").text = str(ymin)
        ET.SubElement(bndbox, "ymax").text = str(ymax)
        
        tree = ET.ElementTree(root)
        tree.write("./annotation/"+filename+".xml")
        
    else:
        root = ET.Element("annotation")
        ET.SubElement(root, "folder").text = folder
        ET.SubElement(root, "filename").text = filename+".jpg"
        ET.SubElement(root, "path").text = path+filename+".jpg"
        source = ET.SubElement(root, "source")
        ET.SubElement(source, "database").text = "open_image_v4"
        size = ET.SubElement(root, "size")
        ET.SubElement(size, "width").text = str(width)
        ET.SubElement(size, "height").text = str(height)
        ET.SubElement(size, "depth").text = str(depth)
        ET.SubElement(root, "segmented").text = "Unspecified"
        obj = ET.SubElement(root, "object")
        ET.SubElement(obj, "name").text = obj_name
        ET.SubElement(obj, "pose").text = "Unknown"
        ET.SubElement(obj, "truncated").text = truncated
        ET.SubElement(obj, "difficult").text = '0'
        ET.SubElement(obj, "occuluded").text = occluded
        bndbox = ET.SubElement(obj, "bndbox")
        ET.SubElement(bndbox, "xmin").text = str(xmin)
        ET.SubElement(bndbox, "xmax").text = str(xmax)
        ET.SubElement(bndbox, "ymin").text = str(ymin)
        ET.SubElement(bndbox, "ymax").text = str(ymax)
        
        tree = ET.ElementTree(root)
        tree.write("./annotation/"+filename+".xml")

with open('./train-annotations-bbox.csv', newline='') as csvfile:
    img_infos = csv.reader(csvfile, delimiter=',', quotechar='|')
    for img_info in img_infos:
        if img_info[2] in CLASS_LIST:
            if (os.path.isfile('./images/'+img_info[0]+'.jpg')):
                img = cv2.imread('./images/'+img_info[0]+'.jpg',1)
                if img_info[2]=="/m/0ftb8":
                    obj_name='sunflower'
                elif img_info[2]=="/m/01g317":
                    obj_name='person'
                    
                if img_info[9]=="1":
                    truncated='1'
                elif img_info[9]=="0":
                    truncated='0'
                    
                if img_info[8]=="1":
                    occluded='1'
                elif img_info[8]=="0":
                    occluded='0'
                    
                write_xml_file(tmp,'images',img_info[0],os.getcwd()+'/images/',img.shape[1],img.shape[0],img.shape[2],obj_name,truncated,occluded,int(img.shape[1]*float(img_info[4])),int(img.shape[1]*float(img_info[5])),int(img.shape[0]*float(img_info[6])),int(img.shape[0]*float(img_info[7])))
                tmp = img_info[0]
            
            