dict = {'c': 97,'a':96, 'b':98}
for i in sorted(dict):
    print (dict[i])

# n = int(input("enter__3"))
# total = (n*(n +1))/2
# print(total)

a = int(input("enter for a: "))
b = int(input("enter for b0: "))

if a <= 0:
    b = b +1
else:
    a=a+1

if a>0 and b>0:
    print("W")
elif a>0:
    print("X")
if b >0:
    print("Y")
else:
    print("Z")

# " apple is a fruit " [-9:-4]

# a = divmod(10,20)
# print(a)



print("My Calculator")
a = int(input("Enter Num-1:"))
b = int(input("Enter Num-2:"))

choice = int(input("1. Add \n 2.Subtract \n 3. Multply \n 4. Divide"))
if (choice == 1):
    print(a+b)
elif(choice == 2):
    print(a-b)
elif(choice == 3):
    print(a*b)
elif(choice == 4):
    print(a/b)
else:
    print("Choose only from 1-4")




















