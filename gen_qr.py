import uuid
import qrcode
import string
#from PIL import Image
import urllib
import random

path="/home/harsha/5000QR/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4,
)

def rand():
	u= ''.join(random.SystemRandom().choice(string.ascii_uppercase+string.digits+string.ascii_lowercase)for _ in range(5))
	return u

def randgen():
	u=str(uuid.uuid4())
	x=u[:5]
	x=x.replace("-","")
	#x=x.lower()
	return x
for i in range(0,5000):
	y=rand()
	z="C"+y
	print z+str(i)
	#image=Image.save(http://qrickit.com/api/qr?d=&addtext=&qrsize=150&t=p&e=m)	
#	image = urllib.URLopener()
#	image.retrieve("http://qrickit.com/api/qr?d="+z+"&addtext="+z+"&qrsize=150&t=p&e=m",path+z+".png")
	qr.add_data(z)
	qr.make(fit=True)
	img = qr.make_image()
	img.save("/home/harsha/5000QR/"+z+".png")
	qr.clear()
	

