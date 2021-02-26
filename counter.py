from collections import Counter


a = Counter()
b = Counter('abrakadabra')
c = Counter({'red': 2, 'blue': 4})
d = Counter(cats=4, dogs=5)

print(a, b, c, d, sep='\n')

print('-' * 20)

print(b['a'])
print(b['z'])
print(b)
b['z'] = -1
print(b)
print(b['z'])

print('-' * 20)

print(list(b.elements()))

print(b.most_common(2))

print('-' * 20)

g = Counter(a=4, b=6, c=-2, d=0)
f = Counter(a=1, b=2, c=3, d=-2)

g.subtract(f)
g.update(f)
print(g)

print('-' * 20)

x = Counter(a=3, b=1)
y = Counter(a=1, b=2)

print(x + y)
print(x - y)
print(x & y)
print(x | y)

print('-' * 20)

z = Counter(a=2, b=-4)
print(+z)
print(-z)

print('-' * 20)

print(g)

print(set(g))
print(dict(g))
print(list(g))

print('-' * 20)

g.clear()
print(g)
