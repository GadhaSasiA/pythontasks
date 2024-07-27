a={1,2,3,4,5}
a.add(6)
c=a.copy()
print(a)
print(c)

b={1,12,32,24,15}
b.clear()
print(b)


a={1,2,3,4,5,6,7,8}
b={1,12,32,24,15}
union=a.union(b)
i=a.intersection(b)
a.discard(8)
d=a.difference(b)
print(union)
print(i)
print(a)
print(d)


a={1,2,3,4,5}
b={1,2,3}
c={1,2,3,4}
print(a.issubset(b))
print(a.issubset(c))