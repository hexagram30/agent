class PriorityDictionary(dict):
    '''
    This data structure acts almost like a dictionary, with two modifications:
    First, D.smallest() returns the value x minimizing D[x]. For this to work
    correctly, all values D[x] stored in the dictionary must be comparable.
    Second, iterating "for x in D" finds and removes the items from D in sorted
    order. Each item is not removed until the next item is requested, so D[x]
    will still return a useful value until the next iteration of the for-loop.

    # Priority dictionary using binary heaps
    # David Eppstein, UC Irvine, 8 Mar 2002

    '''
    def __init__(self):
        '''
        Initialize priorityDictionary by creating binary heap
        of pairs (value,key).  Note that changing or removing a dict entry will
        not remove the old pair from the heap until it is found by smallest() or
        until the heap is rebuilt.
        '''
        self.__heap = []
        dict.__init__(self)

    def smallest(self):
        '''Find smallest item after removing deleted items from heap.'''
        if len(self) == 0:
            raise IndexError, "smallest of empty priorityDictionary"
        heap = self.__heap
        while heap[0][1] not in self or self[heap[0][1]] != heap[0][0]:
            lastItem = heap.pop()
            insertionPoint = 0
            while 1:
                smallChild = 2*insertionPoint+1
                if smallChild+1 < len(heap) and \
                        heap[smallChild] > heap[smallChild+1]:
                    smallChild += 1
                if smallChild >= len(heap) or lastItem <= heap[smallChild]:
                    heap[insertionPoint] = lastItem
                    break
                heap[insertionPoint] = heap[smallChild]
                insertionPoint = smallChild
        return heap[0][1]
	
    def __iter__(self):
        '''Create destructive sorted iterator of priorityDictionary.'''
        def iterfn():
            while len(self) > 0:
                x = self.smallest()
                yield x
                del self[x]
        return iterfn()
	
    def __setitem__(self,key,val):
        '''
        Change value stored in dictionary and add corresponding
        pair to heap.  Rebuilds the heap if the number of deleted items grows
        too large, to avoid memory leakage.'''
        dict.__setitem__(self,key,val)
        heap = self.__heap
        if len(heap) > 2 * len(self):
            self.__heap = [(v,k) for k,v in self.iteritems()]
            self.__heap.sort()  # builtin sort likely faster than O(n) heapify
        else:
            newPair = (val,key)
            insertionPoint = len(heap)
            heap.append(None)
            while insertionPoint > 0 and \
                    newPair < heap[(insertionPoint-1)//2]:
                heap[insertionPoint] = heap[(insertionPoint-1)//2]
                insertionPoint = (insertionPoint-1)//2
            heap[insertionPoint] = newPair
	
    def setdefault(self,key,val):
        '''Reimplement setdefault to call our customized __setitem__.'''
        if key not in self:
            self[key] = val
        return self[key]

class UnionFind:
    '''
    Union Find data structure. Modified from Josiah Carlson's code,
    http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/215912
    to allow arbitrarily many arguments in unions, use [] syntax for finds,
    and eliminate unnecessary code.

    # Find maximum cardinality matching in general undirected graph
    # D. Eppstein, UC Irvine, 6 Sep 2003

    '''

    def __init__(self):
        self.weights = {}
        self.parents = {}

    def __getitem__(self, object):
        '''
        Find the root of the set that an object is in.  Object must be 
        hashable; previously unknown objects become new singleton sets.
        '''
        # check for previously unknown object
        if object not in self.parents:
            self.parents[object] = object
            self.weights[object] = 1
            return object
        
        # find path of objects leading to the root
        path = [object]
        root = self.parents[object]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]
        
        # compress the path and return
        for ancestor in path:
            self.parents[ancestor] = root
        return root

    def union(self, *objects):
        '''
        Find the sets containing the given objects and merge them all.
        '''
        roots = [self[x] for x in objects]
        heaviest = max([(self.weights[r],r) for r in roots])[1]
        for r in roots:
            if r != heaviest:
                self.weights[heaviest] += self.weights[r]
                self.parents[r] = heaviest

class KeyedSet(dict):
    """
    A set class for handling collections of arbitrary objects that have unique,
    and hashable 'id' attributes.  Set items are stored as values in a
    dictionary, with ids as keys.  There is no requirement for set items to be
    hashable.  The class requires a 1 to 1 mapping between objects and their
    ids, and is designed for cases where access to items via a key lookup is
    also desirable.

    For some applications it is fairly natural to assign distinct objects
    distinct 'id' attributes. E.g. nodes in a graph. In some cases it is useful
    (or at least I find it so) to be able to contain such items in sets (and
    perform set operations) whilst also allowing access via object id.

    Use is almost identical to that of the built in set class. The only
    differences (that I am aware of) are that the pop() method, when supplied
    with appropriate arguments, calls the dictionary pop() method, rather than
    popping an arbitrary item; and the __repr__() method returns string
    representations of the keys (ids), rather than values (items). Almost all
    dictionary methods are also available. 'k in a' does not work identically to
    dictionaries as this checks whether item k is in a.values() (or rather that
    k.id is in a.keys()). Iterating over the set iterates over the values,
    rather than keys. But the availability of has_key() and iterkeys() ensures
    that a KeyedSet maintains all the basic functionality of a dictionary when
    required.

    # Submitter: Duncan Smith 
    # Last Updated: 2004/07/07 

    """

    def __init__(self, items=None):
        if items is not None:
            for item in items:
                self[item.id] = item

    def add(self, item):
        self[item.id] = item

    def remove(self, item):
        del self[item.id]

    def __contains__(self, item):
        try:
            return self.has_key(item.id)
        except AttributeError:
            return False

    def __iter__(self):
        return self.itervalues()

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.keys())

    def __cmp__(self, other):
        raise TypeError, "can't compare KeyedSets using cmp()"

    def issubset(self, other):
        self._binary_check(other)
        if len(self) > len(other):
            return False
        else:
            for key in self.iterkeys():
                if not other.has_key(key):
                    return False
        return True

    def issuperset(self, other):
        self._binary_check(other)
        return other.issubset(self)

    __le__ = issubset
    __ge__ = issuperset

    def __lt__(self, other):
        self._binary_check(other)
        return len(self) < len(other) and self.issubset(other)

    def __gt__(self, other):
        self._binary_check(other)
        return len(self) > len(other) and self.issuperset(other)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return len(self) == len(other) and self.issubset(other)
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self == other
        else:
            return True

    def union(self, other):
        res = self.copy()
        for item in other:
            res.add(item)
        return res

    def intersection(self, other):
        res = self.__class__()
        if not isinstance(other, self.__class__):
            other = self.__class__(other)
        if len(self) > len(other):
            for item in other:
                if item in self:
                    res.add(item)
        else:
            for item in self:
                if item in other:
                    res.add(item)
        return res

    def difference(self, other):
        res = self.copy()
        for item in other:
            if item in res:
                res.remove(item)
        return res

    def symmetric_difference(self, other):
        res = self.copy()
        if not isinstance(other, self.__class__):
            other = self.__class__(other)
        for item in other:
            if item in self:
                res.remove(item)
            else:
                res.add(item)
        return res

    def __or__(self, other):
        self._binary_check(other)
        return self.union(other)

    def __and__(self, other):
        self._binary_check(other)
        return self.intersection(other)

    def __sub__(self, other):
        self._binary_check(other) 
        return self.difference(other)

    def __xor__(self, other):
        self._binary_check(other)
        return self.symmetric_difference(other)

    def _binary_check(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError, "Binary operation only permitted between KeyedSets"

    def copy(self):
        res = self.__class__()
        res.update(self)
        return res

    def union_update(self, other):
        if isinstance(other, (self.__class__, dict)):
            self.update(other)
        else:
            for item in other:
                self.add(item)

    def intersection_update(self, other):
        if not isinstance(other, self.__class__):
            other = self.__class__(other)
        self &= other

    def difference_update(self, other):
        for item in other:
            self.discard(item)

    def symmetric_difference_update(self, other):
        if not isinstance(other, self.__class__):
            other = self.__class__(other)
        for item in other:
            if item in self:
                self.remove(item)
            else:
                self.add(item)

    def __ior__(self, other):
        self._binary_check(other)
        self.union_update(other)
        return self

    def __iand__(self, other):
        self._binary_check(other)
        intersect = self & other
        self.clear()
        self.update(intersect)
        return self

    def __isub__(self, other):
        self._binary_check(other)
        self.difference_update(other)
        return self

    def __ixor__(self, other):
        self._binary_check(other)
        self.symmetric_difference_update(other)
        return self

    def discard(self, item):
        try:
            self.remove(item)
        except KeyError:
            pass

    def pop(self, *args):
        if args:
            return super(self.__class__, self).pop(*args)
        else:
            return self.popitem()[1]

    def update(self, other):
        if isinstance(other, (self.__class__, dict)):
            super(self.__class__, self).update(other)
        else:
            for item in other:
                self.add(item)

