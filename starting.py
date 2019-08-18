print("Hello Python")

a=10
b=10.5
print(a,b,type(a))
print(a)

print(int(b))
print(8<79)

print(float("2158.055"))

print(bin(107),hex(19),oct(7))
'''
List Set  & Dictionary
Dictionary  --  Map 
'''
'''
String
'''
s="this is  a string"
print(s)
s1='''   You are
printing multiple
line   
'''

print(s1[11])
#repetetion
print(s*2)

#length
print(len(s1))
#Slice string
print(s[0:5],s[0:],s[:7])
'''
Minus starts from last
'''
print(s[-3:-1])
#2step
print(s[0:9:2])
#reverse a string
print(s[::-1])
#strip off the spaces  lstrip is also  vailable along with rstrip
print(s1.strip( ))
#find
s.find("is")
print(s.find('is',0,len(s)))
print(s.count('is'))
print(s.replace('string','replaced string'))
print(s.upper() , s.lower(), s.title())

#assignment
a=10
b=20.54
c=True
d = 'I am the best'
print(a)
print(b)
print(c)
print(d)
