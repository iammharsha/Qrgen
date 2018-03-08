from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os
path='/home/harsha/5000QR'
i=0
for file in os.listdir(path):
   if file.endswith(".png"):
        print(file)
	i=i+1
	print(i)
	img = Image.open('/home/harsha/5000QR/'+file, 'r')
	img_w, img_h = img.size
	img1=img.resize((1750,1750),Image.ANTIALIAS)
	img1_w,img1_h=img1.size
	template=Image.open('/home/harsha/Downloads/gowtham-Nija-2.png')
	temp_w,temp_h=template.size
	offset=((temp_w - img1_w)/2 , (temp_h - img1_h) / 2)
	template.paste(img1,offset)


#background = Image.new('RGBA', (230, 353), (255, 255, 255, 255))
#bg_w, bg_h = background.size
#offset = ((bg_w - img_w) , (bg_h - img_h) / 2)
#background.paste(img, offset)
#draw = ImageDraw.Draw(template)
# font = ImageFont.truetype(<font-file>, <font-size>)
#font = ImageFont.truetype("/usr/share/fonts/truetype/LiberationMono-Regular.ttf", 16)
# draw.text((x, y),"Sample Text",(r,g,b))
#draw.text((50,temp_h-50),"Sample Text",(0,0,0),font=font)
	template.save('/home/harsha/5000QR/'+file,subsampling=0,quality=100)
