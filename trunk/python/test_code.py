from numarray import outerproduct, outerproduct
from adytum.personality import myersbriggs as mb

rp = mb.REFERENCE_PAIRS
me = mb.getTempermentType('INTP')
mg = mb.getTempermentType('ENTJ')
el = mb.getTempermentType('INTJ')

outerproduct(me, mg)
diagonal(outerproduct(mg, me))
me * mg
me + mg

mb.getProperOrder('intp')
mb.getProperOrder('pnti')
