flag = True
number = int(input("Enter a number"))
for x in range(2,number-1) :
    if number % x == 0 :
        flag = False
if flag :
    print("Prime")
