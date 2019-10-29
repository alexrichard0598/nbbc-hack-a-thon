from PIL import Image

im = Image.open('image.png')
pix = im.load()
height = im.height
y = 0
Message = ""
while (y < height):
    RGBAVal = pix[0, y]
    BlueVal = RGBAVal[2]
    Message += chr(BlueVal)
    y += 1

path = "C:\\Users\\Alex Richard\\Github\\nbbc-hack-a-thon\\decoder\\message.txt"
newf = open(path, 'w')
newf.write(Message)
