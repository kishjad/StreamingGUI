from PIL import Image
im =  Image.open('./images/hulu-icon.png')

im = im.resize((206,206))
im.save('./images/hulu-icon.png',quality=95)

width,height = im.size

print (width,height)
