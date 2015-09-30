'''
This part of the program is the encoder.
It will encode our message into the image.
'''

#Required module: PIL
from PIL import Image

#Definition to encode message into image.
def encode_message(img, msg):
    #Check message length
    limit = len(msg)

    if(limit>255):
        print("The message is too long. Keep it under 255 characters.")
        return False
    if(img.mode != "RGB"):
        print("Image needs to be in RBG mode.")
        return False

#Whatever image we decide to use converted to .bmp
ori_img = "fish.bmp" 
img = Image.open(ori_img)

#Message to encode into image
msg = "Something"

encode_message(img,msg)
