/*
29 March 2002

Copyright 2001, 2002 Brown University, Providence, RI.

All Rights Reserved

Permission to use, copy, modify, and distribute this software and its
documentation for any purpose other than its incorporation into a
commercial product is hereby granted without fee, provided that the
above copyright notice appear in all copies and that both that
copyright notice and this permission notice appear in supporting
documentation, and that the name of Brown University not be used in
advertising or publicity pertaining to distribution of the software
without specific, written prior permission.

BROWN UNIVERSITY DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR ANY
PARTICULAR PURPOSE.  IN NO EVENT SHALL BROWN UNIVERSITY BE LIABLE FOR
ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

*/

%module graphviz
%{
#include "agraph.h"
%}

%typemap(python, in) FILE* {
    if (!PyFile_Check($source)) {
        PyErr_SetString(PyExc_TypeError, "not a file");
	return NULL;
    }
    $target = PyFile_AsFile($source);
}

%typemap(python, in) char* {
    if ($source == Py_None) {
        $target = 0;
    } else if (!PyString_Check($source)) {
	    PyErr_SetString(PyExc_TypeError, "not a string");
	    return NULL;
    } else $target = PyString_AsString($source);
}

%typemap(python, out) char * {
    $target = Py_BuildValue("s", $source);
}

/* GRAPHS */
 Agraph_t        *agopen(char *name, Agdesc_t kind, Agdisc_t *disc);
 int             agclose(Agraph_t *g);
 Agraph_t        *agread(FILE *file, Agdisc_t *);
 Agraph_t        *agconcat(Agraph_t *g, void *chan, Agdisc_t *disc);
 int             agwrite(Agraph_t *g, FILE *file);
 int             agnnodes(Agraph_t *g),agnedges(Agraph_t *g);

/* SUBGRAPHS */
 Agraph_t        *agsubg(Agraph_t *g, char *name, int createflag);
 Agraph_t        *agfstsubg(Agraph_t *g), *agnxtsubg(Agraph_t *);
 Agraph_t        *agparent(Agraph_t *g),  *agroot(Agraph_t *g);
 long            agdelsubg(Agraph_t *g, Agraph_t *sub);


/* NODES */
 Agnode_t        *agnode(Agraph_t *g, char *name, int createflag);
 Agnode_t        *agidnode(Agraph_t *g, ulong id, int createflag);
 Agnode_t        *agsubnode(Agraph_t *g, Agnode_t *n, int createflag);
 Agnode_t        *agfstnode(Agraph_t *g);
 Agnode_t        *agnxtnode(Agnode_t *n);
 int             agdelnode(Agnode_t *n);
 /*
 int             agrename(Agraph_t *g, Agnode_t *n, char *newname);
 */
 int             agdegree(Agnode_t *n, int use_inedges, int use_outedges);


/* EDGES */
 Agedge_t        *agedge(Agnode_t *t, Agnode_t *h, char *name, int createflag);
 Agedge_t        *agsubedge(Agraph_t *g, Agedge_t *e, int createflag);
 int             agdeledge(Agedge_t *e);

 Agnode_t        *aghead(Agedge_t *e);
 Agnode_t        *agtail(Agedge_t *e);
 Agedge_t        *agfstedge(Agnode_t *n);
 Agedge_t        *agnxtedge(Agedge_t *e, Agnode_t *n);
 Agedge_t        *agfstin(Agnode_t *n);
 Agedge_t        *agnxtin(Agedge_t *e);
 Agedge_t        *agfstout(Agnode_t *n);
 Agedge_t        *agnxtout(Agedge_t *e);

/* FLATTENED LISTS */
/*
void             agflatten(Agraph_t *graph, int flag);
 Agnode_t        *agfstn(Agraph_t *g); 
 Agnode_t        *agnxtn(Agnode_t *n);
 Agedge_t        *agfout(Agnode_t *n);
 Agedge_t        *agfin(Agnode_t *n);
 Agedge_t        *agnxte(Agedge_t *e);
*/

/* STRING ATTRIBUTES */
 Agsym_t     *agattr(Agraph_t *g, int kind, char *name, char *value);
 Agsym_t     *agnxtattr(Agraph_t *g, int kind, Agsym_t *attr);
 char        *agget(void *obj, char *name);
 char        *agxget(void *obj, Agsym_t *sym);
 int         agset(void *obj, char *name, char *value);
 int         agxset(void *obj, Agsym_t *sym, char *value);


/* RECORDS */
/*
 void        *agnewrec(Agraph_t *g, void *obj, char *name, unsigned int size);
 Agrec_t     *aggetrec(void *obj, char *name, int move_to_front);
 int         agdelrec(void *obj, char *name);
*/

/* CALLBACKS */
/*
int agpopdisc(Agraph_t *g, Agcbdisc_t *);
 void        agpushdisc(Agraph_t *g, Agcbdisc_t *disc, void *state);
 void        agmethod(Agraph_t *g, void *obj, Agcbdisc_t *disc, int initflag);
*/

/* MEMORY */
/*
 void      *agalloc(Agraph_t *g, size_t request);
 void      *agrealloc(Agraph_t *g, void *ptr, size_t oldsize, size_t newsize);
 void      agfree(Agraph_t *g, void *ptr);
*/


/* GENERIC OBJECTS */
 Agraph_t  *agraphof(void*);
 char      *agnameof(void*);
 int            agisarootobj(void*);
 Agrec_t        *AGDATA(void *obj);
 ulong          AGID(void *obj);
 int            AGTYPE(void *obj);

/* Constants */
Agdesc_t Agdirected, Agstrictdirected, Agundirected, Agstrictundirected;

#define AGRAPH                          0               /* can't exceed 2 bits. see Agtag_t. */
#define AGNODE                          1
#define AGOUTEDGE                       2
#define AGINEDGE                        3               /* (1 << 1) indicates an edge tag.   */
#define AGEDGE                          AGOUTEDGE       /* synonym in object kind args */
