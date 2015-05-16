import math
from PIL import Image


im1 = Image.open("a512.png")
im2 = Image.open("chess-512.png")
assert im1.size == im2.size
pix1 = im1.load()
pix2 = im2.load()


imdst = Image.new("RGB", im1.size, (0,0,0))
pixdst = imdst.load()

for x in range(im1.size[0]):
  for y in range(im1.size[1]):
    if pix1[x, y] == (0, 0, 0):
       p = (0, 0, 0)
    else:
       p = pix2[x, y]
    pixdst[x, y] = p

imdst.save("AxCH.png", "PNG")
