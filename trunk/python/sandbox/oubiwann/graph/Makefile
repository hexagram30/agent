PYTHON_INCLUDES=/System/Library/Frameworks/Python.framework/Versions/2.3/include/python2.3
GRAPHVIZ_LIBS=/sw/lib/graphviz
GRAPHVIZ_INCS=/sw/includes/graphviz
APPLE_FRAMEWORKS=/System/Library/Frameworks



graphviz.so: agraph.so cdt.so gv_wrap.o
	gcc -L${GRAPHVIZ_LIBS} -F${APPLE_FRAMEWORKS} \
	-shared agraph.so cdt.so gv_wrap.o -o graphviz.so

gv_wrap.o:gv.i
	swig -python gv.i 
	gcc -c -I. -fPIC -DPIC -I${PYTHON_INCLUDES} gv_wrap.c 
