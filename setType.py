s={1,2,3}
print(s)
'''
set is not in ordered mode so no index,slicing etc
'''
s.update([8,9])

f=frozenset(s)
#range normaly for staring from zero we just need to give end limit
r = range(1,15,3)
for i in r:
    print(i)
b=bytes(s)
print(type(b))
#indexing addition modification is not possible byte array
print(bytearray(s))

dict={1:"kk",2:"qwer"}

v=dict.values()
for i in v:
    print(i)

a=dict[1]


#assignment
lst1 = ["india","france","UK"]
lst1.append("USA")
del(lst1[3])
lst1.insert(2,"USA")

s= {"india","france","UK"}
s.add("USA")
s.remove("UK")
