edge_power = 9

power = 2*edge_power

imgwidth = 2**edge_power
imgheight = 2**edge_power


import math
from PIL import Image

def ThueMorse(x):
  if x==0: return 0
  return sum([ ((x>>i)&1) for i in range(int(math.log(x, 2))+1) ])&1

image = Image.new("RGB", (imgwidth, imgheight), (0,0,0))
pix = image.load()

for i in xrange(2**power):
  x = (i%imgwidth)
  y = (i/imgheight)
  assert x<imgwidth, x
  assert y<imgheight, y
  if ThueMorse(i) == 1:
    pix[x, y] = (255, 255, 0)
  else:
    pix[x, y] = (0, 255, 0)

image.save("thue-morse-%d.png"%imgwidth, "PNG")
