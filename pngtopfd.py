import os
from os import listdir
from os.path import isfile, join 
from pgmagick import Image

mypath = "/home/harsha/5000QR/" # path to your Image directory 
i=0
for each_file in listdir(mypath):
    if isfile(join(mypath,each_file)):
        print each_file+" "+str(i)
	image_path = os.path.join(mypath,each_file)
        pdf_path =  os.path.join('/home/harsha/5000QR/',each_file.rsplit('.', 1)[0]+'.pdf')
        img = Image(image_path)
        img.write(pdf_path)
	i=i+1
	print i
