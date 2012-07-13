# XXX convert this whole file to unit tests
from numpy.numarray import outerproduct, outerproduct, diagonal

from innoth.personality.myersbriggs import MyersBriggs as mb, REFERENCE_PAIRS

rp = REFERENCE_PAIRS
me = mb.getTemperamentArray('INTP')
mg = mb.getTemperamentArray('ENTJ')
el = mb.getTemperamentArray('INTJ')

print outerproduct(me, mg)
print diagonal(outerproduct(mg, me))
print me * mg
print me + mg

print mb.getProperOrder('intp')
print mb.getProperOrder('pnti')

for i in [1,-1]:
  for j in [1,-1]:
    for k in [1,-1]:
      for l in [1,-1]:
        print mb.getTemperamentString([i,j,k,l])


def getStats(alist):
  seen = {0:0, 1:0}
  [ seen.update({x:seen[x]+1}) for x in alist ]
  return seen
