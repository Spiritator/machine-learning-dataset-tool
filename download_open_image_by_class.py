import csv
import os, sys

dir = sys.path[0]
save_dir = dir + "/person/"
tmp = []
CLASS_LIST = ("/m/01g317") # person: "/m/01g317", sunflower: "/m/0ftb8"

with open(dir + '/train-annotations-bbox.csv', newline='') as csvfile:
	bboxs = csv.reader(csvfile, delimiter=',', quotechar='|')
	for bbox in bboxs:
		if bbox[0] == tmp:
			continue #Avoid downloading one image many times for the image which contains multiple target classes
		if bbox[2] in CLASS_LIST:
			tmp = bbox[0]
			os.system("gsutil cp gs://open-images-dataset/train/%s.jpg %s.jpg"%(bbox[0], save_dir+bbox[0]))