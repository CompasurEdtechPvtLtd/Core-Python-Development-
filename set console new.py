Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> "SET"
'SET'
>>> #unordered Data collection
>>> x = {'a','b','c','d'}
>>> #no indexing
>>> x
{'b', 'd', 'c', 'a'}
>>> #set cannot have any duplicate value
>>> x = {'a','b','a','b','c','c'}
>>> x
{'c', 'b', 'a'}
>>> x = {}#dictionary
>>> type(x)
<class 'dict'>
>>> x = set()
>>> type(x)
<class 'set'>
>>> x.add('a')
>>> x
{'a'}
>>> x.add('b')
>>> x
{'b', 'a'}
>>> x.add('c')
>>> x
{'c', 'b', 'a'}
>>> x.discard('c')
>>> x
{'b', 'a'}
>>> x.clear()
>>> x
set()
>>> set1={'a','b','c'}
>>> set2={'b','c','d'}
>>> set1.union(set2)
{'c', 'd', 'b', 'a'}
>>> set1.intersection(set2)
{'b', 'c'}
>>> 
>>> set1
{'c', 'b', 'a'}
>>> set2
{'b', 'd', 'c'}
>>> set1-set2
{'a'}
>>> set2-set1
{'d'}
>>> set1
{'c', 'b', 'a'}
>>> set2
{'b', 'd', 'c'}
>>> set1.update(set2)
>>> set1
{'c', 'd', 'b', 'a'}
>>> set1.intersection_update(set2)
>>> set1
{'c', 'b', 'd'}
>>> set1.difference_update(set2)
>>> set1
set()
>>> 