import csv
import os, sys

dir = sys.path[0]
class_name_list=['tomato'  ,'elephant'  ,'pizza'   ,'armadillo','tiger'   ,'dolphin' ,'centipede','sheep'   ,'bear'    ,'frog'    ,'rabbit'  ,'sword'   ,'eagle'   ,'rose'    ,'hippo'   ,'airplane','spider'  ,'ladybug' ,'lobster' ,'alpaca' ]
class_id_list=  ['/m/07j87','/m/0bwd_0j','/m/0663v','/m/0xfy'  ,'/m/07dm6','/m/02hj4','/m/019h78','/m/07bgp','/m/01dws','/m/09ld4','/m/06mf6','/m/06y5r','/m/09csl','/m/06m11','/m/09f20','/m/0cmf2','/m/09kmb','/m/0gj37','/m/0cjq5','/m/0pcr']
num_train=2000
num_validation=200
num_test=100
tmp = []

class_item=dict(zip(class_id_list, class_name_list))

# training set
save_dir = dir + '/dataset/train/'
class_count=[0 for _ in range(20)]
with open(dir + '/train-annotations-human-imagelabels.csv', newline='') as csvfile:
    bboxs = csv.reader(csvfile, delimiter=',', quotechar='|')
    for bbox in bboxs:
        if bbox[0] == tmp:
            continue #Avoid downloading one image many times for the image which contains multiple target classes
        if bbox[2] in class_id_list:
            idx=class_id_list.index(bbox[2])
            if class_count[idx]>=num_train or bbox[3]!='1':
                continue
            else:
                tmp = bbox[0]
                class_count[idx]+=1
            
                os.system("gsutil cp gs://open-images-dataset/train/%s.jpg %s.jpg"%(bbox[0], save_dir+'/'+class_item[bbox[2]]+'/'+bbox[0]))
        
        if sum(class_count)>=40000:
            break

# validation set
save_dir = dir + '/dataset/validation/'
class_count=[0 for _ in range(20)]
with open(dir + '/validation-annotations-human-imagelabels.csv', newline='') as csvfile:
    bboxs = csv.reader(csvfile, delimiter=',', quotechar='|')
    for bbox in bboxs:
        if bbox[0] == tmp:
            continue #Avoid downloading one image many times for the image which contains multiple target classes
        if bbox[2] in class_id_list:
            idx=class_id_list.index(bbox[2])
            if class_count[idx]>=num_validation or bbox[3]!='1':
                continue
            else:
                tmp = bbox[0]
                class_count[idx]+=1
            
                os.system("gsutil cp gs://open-images-dataset/validation/%s.jpg %s.jpg"%(bbox[0], save_dir+'/'+class_item[bbox[2]]+'/'+bbox[0]))
        
        if sum(class_count)>=4000:
            break    

# test set
save_dir = dir + '/dataset/test/'
class_count=[0 for _ in range(20)]
with open(dir + '/test-annotations-human-imagelabels.csv', newline='') as csvfile:
    bboxs = csv.reader(csvfile, delimiter=',', quotechar='|')
    for bbox in bboxs:
        if bbox[0] == tmp:
            continue #Avoid downloading one image many times for the image which contains multiple target classes
        if bbox[2] in class_id_list:
            idx=class_id_list.index(bbox[2])
            if class_count[idx]>=num_test or bbox[3]!='1':
                continue
            else:
                tmp = bbox[0]
                class_count[idx]+=1
            
                os.system("gsutil cp gs://open-images-dataset/test/%s.jpg %s.jpg"%(bbox[0], save_dir+'/'+class_item[bbox[2]]+'/'+bbox[0]))
        
        if sum(class_count)>=2000:
            break   