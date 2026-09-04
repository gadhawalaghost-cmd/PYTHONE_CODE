# methode are work with set.method().
# thay dont work on indexing

set1={67,37,84,2,5,3,1,}
set2={88,2,5,46,3,90,1}

set1.add(99)
set1.remove(67)
set1.pop()
print(set1)
print(set.union(set2,set1))
print(set.intersection(set2,set1))
set1.clear()
print(set1)