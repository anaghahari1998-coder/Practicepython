d1 = {"id":1, "name":"Anagha"}
print(d1)
print(type(d1))
d2 = dict(a='parrot', b='pigeon')
print(d2)
print(d2.get('a'))   # values can be retrieved using either get function or []
print(d2['a'])
d2['a'] = "peacock"  # to update an existing value
print(d2)
d2.pop('a')
print(d2)
d2['c'] = "crow"  # to add a new value
print(d2)
d3 = {}
print(d3)