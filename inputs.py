'''a,b = 20,9
print(a,b,sep=",")

name = 'abc'
marks = 94.5
print("name is %s, Marks are %.2f"%(name,marks))
print("name is {} marks are {}".format(name,marks))

str = input("string ?")
print(str)'''

#lst = [x for x in input("enter 3 numbers").split()]
lst = [int(x) for x in input("enter 3 numbers").split(',')]
print(lst)
