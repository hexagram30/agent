# 29 March 2002
# Copyright 2001,2002, Brown University, Providence, RI.
# 
# All Rights Reserved
# 
# Permission to use, copy, modify, and distribute this software and its
# documentation for any purpose other than its incorporation into a
# commercial product is hereby granted without fee, provided that the
# above copyright notice appear in all copies and that both that
# copyright notice and this permission notice appear in supporting
# documentation, and that the name of Brown University not be used in
# advertising or publicity pertaining to distribution of the software
# without specific, written prior permission.
# 
# BROWN UNIVERSITY DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
# INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR ANY
# PARTICULAR PURPOSE.  IN NO EVENT SHALL BROWN UNIVERSITY BE LIABLE FOR
# ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from graphviz import *

GraphKind = cvar

class Agraph:
    class Node:
        def __init__(self, anode):
	    self.__dict__["anode"] = anode
	    self.__dict__["inedgeslist"] = None
	    self.__dict__["outedgeslist"] = None

	def __str__(self):
	    return agnameof(self.anode)

	def __cmp__(self,other):
	    return self.anode < other.anode

	def __hash__(self):
	    return hash(self.anode)

	def getAttr(self, name):
	    return agget(self.anode, name)

	def setAttr(self, name, value):
	    return agset(self.anode, name, value)

	def __getattr__(self, name):
	    # when agraph::agget does not find a attribute,
	    # it returns ""
	    # agraph::agset returns -1 though, so we can 
	    # check that.
	    if self.__dict__.has_key(name):
	        return self.__dict__[name]
	    else:
	        val = agget(self.anode, name)
		if val != "": 
		    return val
		else: 
		    if agset(self.anode, name, val) == -1:
			raise AttributeError,"No such attribute: "+name
		    else: return ""

	def __setattr__(self, name, value):
	    if self.__dict__.has_key(name):
	        self.__dict__[name] = value
	    else: 
	        if agset(self.anode, name, str(value)) == -1:
		    raise AttributeError,"No such attribute: "+name
		else: return ""

	def inedges(self):
	    #if self.inedgeslist == None:
	    self.inedgeslist = []
	    a = agfstin(self.anode)
	    while a != None:
		self.inedgeslist.append(Agraph.Edge(a))
		a = agnxtin(a)

	    return tuple(self.inedgeslist)

	def outedges(self):
	    #if self.outedgeslist == None:
	    self.outedgeslist = []
	    a = agfstout(self.anode)
	    while a != None:
		self.outedgeslist.append(Agraph.Edge(a))
		a = agnxtout(a)

	    return tuple(self.outedgeslist)

	def degree(self):
	    return agdegree(self.anode, 1, 1)

	def indegree(self):
	    return agdegree(self.anode, 1, 0)

	def outdegree(self):
	    return agdegree(self.anode, 0, 1)

	def graph(self):
	    return Agraph(agraphof(self.anode))

    class Edge:
        def __init__(self, aedge):
	    self.__dict__["aedge"] = aedge

	def __str__(self):
	    return agnameof(self.aedge)

	def __cmp__(self,other):
	    return self.aedge < other.aedge

	def __hash__(self):
	    return hash(self.aedge)

	def target(self):
	    return Agraph.Node(aghead(self.aedge))

	def source(self):
	    return Agraph.Node(agtail(self.aedge))

	def getAttr(self, name):
	    return agget(self.aedge, name)

	def setAttr(self, name, value):
	    return agset(self.aedge, name, value)

	def __getattr__(self, name):
            # when agraph::agget does not find a attribute,
            # it returns ""
            # agraph::agset returns -1 though, so we can  
            # check that.
            if self.__dict__.has_key(name):
                return self.__dict__[name]
            else:   
                val = agget(self.aedge, name)
                if val != "":  
                    return val
                else:   
                    if agset(self.aedge, name, val) == -1:
                        raise AttributeError,("No such edge attribute: "+name)
                    else: return ""

	def __setattr__(self, name, value):
            if self.__dict__.has_key(name):
                self.__dict__[name] = value 
            else:   
                if agset(self.aedge, name, str(value)) == -1:
                    raise AttributeError,"No such attribute: "+name
		else: return ""

	def graph(self):
	    return Agraph.Agraph(agraphof(self.aedge))

    def __init__(self, agraph = None):
        self.agraph = agraph
	self.opened = 0
	self.subgraphslist = None
	self.nodeslist = None
	self.edgeslist = None
       
    def __del__(self):
        if self.opened: agclose(self.agraph)

    def __str__(self):
	return agnameof(self.agraph)

    def __cmp__(self,other):
	return self.agraph < other.agraph

    def __hash__(self):
	return hash(self.agraph)

    def __getattr__(self, name):
	# when agraph::agget does not find a attribute,
	# it returns ""
	# agraph::agset returns -1 though, so we can 
	# check that.
	if self.__dict__.has_key(name):
	    return self.__dict__[name]
	else:
	    val = agget(self.agraph, name)
	    if val != "": 
		return val
	    else: 
		if agset(self.agraph, name, val) == -1:
		    raise AttributeError,"No such attribute: "+name
		else: return ""

    def read(self, fp):
        self.agraph = agread(fp, None)

    def write(self, fp):
        agwrite(self.agraph, fp)

    def nnodes(self):
        return agnnodes(self.agraph)

    def nedges(self):
        return agnedges(self.agraph)

    def subgraphs(self):
        #if self.subgraphslist == None:
	self.subgraphslist = []
	a = agfstsubg(self.agraph)
	while a:
	    self.subgraphslist.append(Agraph(a))
	    a = agnxtsubg(a)

	return tuple(self.subgraphslist)

    def nodes(self):
        #if self.nodeslist == None:
	self.nodeslist = []
	a = agfstnode(self.agraph)
	while a:
	    self.nodeslist.append(Agraph.Node(a))
	    a = agnxtnode(a)

	return tuple(self.nodeslist)

    def edges(self):
        #if self.edgeslist == None:
	self.edgeslist = []
	nodes = self.nodes()
	for n in nodes:
	    a = agfstin(n.anode)
	    while a:
		self.edgeslist.append(Agraph.Edge(a))
		a = agnxtin(a)

	return tuple(self.edgeslist)

    def getAttr(self, name):
	return agget(self.agraph, name)

    def setAttr(self, name, value):
	return agset(self.agraph, name, value)

    def createNodeAttr(self, name, deflt):
        agattr(self.agraph, AGNODE, name, deflt)

    def createEdgeAttr(self, name, deflt):
        agattr(self.agraph, AGEDGE, name, deflt)

    def createGraphAttr(self, name, deflt):
        agattr(self.agraph, AGRAPH, name, deflt)

    def createNode(self, name):
        return Agraph.Node(agnode(self.agraph, name, 1))

    def findNode(self, name):
        a = agnode(self.agraph, name, 0)
	if a == None: return None
        else: return Agraph.Node(a)

    def delNode(self, node):
        agdelnode(node.anode)

    def createEdge(self, node_from, node_to, name):
        return Agraph.Edge(agedge(node_from.anode, node_to.anode, name, 1))

    def findEdge(self, node_from, node_to, name):
        a = agedge(node_from.anode, node_to.anode, name, 0)
	if a == None: return None
        else: return Agraph.Edge(a)

    def delEdge(self, edge):
        agdeledge(edge.aedge)

    def createSubgraph(self, name):
        return Agraph(agsubg(self.agraph, name, 1))

    def findSubgraph(self, name):
	a = agsubg(self.agraph, name, 0)
	if a == None: return None
	else: return Agraph(a)

    def delSubgraph(self, agraph):
        agdelsubg(self.agraph, agraph.agraph)

    def graph(self):
	return Agraph(agraphof(self.agraph))

    def parent(self):
        return Agraph(agparent(self.agraph))

    def root(self):
        return Agraph(agroot(self.agraph))

    def isroot(self):
        return agisarootobj(self.agraph)


if __name__ == '__main__':
    a = Agraph()
    f = open('moo.dot','r')
    a.read(f)

    a.createNode("whoknows")
    for i in a.nodes():
	#print i
	print i.getAttr("manos")
	for j in i.inedges():
	    pass
	    #print j

    n = a.findNode("lll")
    print "lala"
    print agget(n.anode, "name")
    print "lala"

    print a.findNode("lll")
    print a.findNode("whoknows")

    e = a.createEdge(a.findNode("lll"), a.findNode("whoknows"), "hello")
    e = a.createEdge(a.findNode("lll"), a.findNode("whoknows"), "mine")
    e = a.createEdge(a.findNode("whoknows"), a.findNode("lll"), "again")
    print e
    print "%", a.findEdge(a.findNode("lll"), a.findNode("whoknows"), None)
    print "$", a.findEdge(a.findNode("lll"), a.findNode("whoknows"), None)
    e =  a.findEdge(a.findNode("goo"), a.findNode("whoknows"), None)
    print "%^&",e

    #a.delNode(n)
    g = open('roo.dot','w')
    a.write(g)
