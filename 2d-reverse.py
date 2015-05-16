filename = "AxCH.png"

import math, numpy
from PIL import Image
import os.path

def bitreverse(n, l):
  r = 0
  for i in range(l):
    if n&(1<<(l-i-1)) != 0:
      r = r | (1<<i)
  return r

assert bin(bitreverse(1, 4))=='0b1000'
assert bin(bitreverse(2, 4))=='0b100'
assert bin(bitreverse(5, 4))=='0b1010'

print "Loading image..."
imsrc = Image.open(filename)
assert imsrc.size[0] == imsrc.size[1]
assert (imsrc.size[0]&(imsrc.size[0]-1)) == 0 # size is power of 2
pixsrc = imsrc.load()

imdst = Image.new(imsrc.mode, imsrc.size)
pixdst = imdst.load()

N = imsrc.size[0]
L = int(math.log(N, 2))
r = [0] * N
for n in range(N):
  r[n] = bitreverse(n, L)

print "Transforming image..."
for y in xrange(N):
  for x in xrange(N):
    pixdst[r[x], r[y]] = pixsrc[x, y]

dstfilename, _ = os.path.splitext(filename)
dstfilename = dstfilename + "-r2.png"
print "Saving image to", dstfilename
imdst.save(dstfilename, "PNG")
