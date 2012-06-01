from numarray import outerproduct, outerproduct, diagonal
from adytum.personality import myersbriggs as mb

rp = mb.REFERENCE_PAIRS
me = mb.getTemperamentArray('INTP')
mg = mb.getTemperamentArray('ENTJ')
el = mb.getTemperamentArray('INTJ')

outerproduct(me, mg)
diagonal(outerproduct(mg, me))
me * mg
me + mg

mb.getProperOrder('intp')
mb.getProperOrder('pnti')

for i in [1,-1]:
  for j in [1,-1]:
    for k in [1,-1]:
      for l in [1,-1]:
        mb.getTemperamentString([i,j,k,l])


def getStats(alist):
  seen = {0:0, 1:0}
  [ seen.update({x:seen[x]+1}) for x in alist ]
  return seen

