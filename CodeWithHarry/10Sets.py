s = set()
# print(type(s))

l1 = [1, 2, 3, 4, 5]
new_set = set(l1)
# print(type(new_set))

s.add(1)
s.add(1)
s.add(1)
# print(s)

s1 = {1, 2, 3}
print(type(s1))
s2 = {1, 2}
print(type(s2))

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.isdisjoint(s2))
print(min(s1))
print(max(s2))

s1.remove(1)
print(s1)
