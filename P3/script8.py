import cProfile

mylist = range(0,2000000)
not_reverse = [x for x in reversed(mylist)].sort()