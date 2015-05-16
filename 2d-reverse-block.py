breaking_power = 6 # power of 2 of number of squares on line

filename = "AxCH-r2.png"

import math, numpy
from PIL import Image
import os.path

def bitreverse(n, l):
  r = 0
  for _ in xrange(l):
    r = 2*r + n%2
    n /= 2
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
NN = imsrc.size[0]
LL = int(math.log(NN, 2))
L = LL - breaking_power
assert L > 0, "Too small block"
N = 2**L
print "Block size is", N

r = [0] * N
for n in range(N):
  r[n] = bitreverse(n, L)

print "Transforming image..."
for h in range(1<<breaking_power):
  for v in range(1<<breaking_power):
    #print "Transforming image", hs[h], vs[v]
    for y in xrange(N):
       for x in xrange(N):
         pixdst[r[x]+h*N, r[y]+v*N] = pixsrc[x+h*N, y+v*N]

dstfilename, _ = os.path.splitext(filename)
dstfilename = dstfilename + "-r2b"+str(N)+".png"
print "Saving image to", dstfilename
imdst.save(dstfilename, "PNG")
