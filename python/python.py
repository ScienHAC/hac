import os,time
from colorama import Fore
print(-23>0)
print(Fore.RED)
age = int(input("enter the age : "))
if age<=12:
    print("Child");
elif age<=19 and age>=13:
    print("teenager")
elif age<= 60 and age>=20:
    print("adult")
else:
    print("Senior Citizen")
a = []
while True:
    b = int(input("Enter the number else type 0: "))
    if b == 0:
        break
    a.append(b)
print(a)
print(max(a))

price = int(input("Enter the price: "))

if (price>1000):
    print(f"The final price of product = {int(price*(90/100))}")
else:
    print(f"The product price is {price}")



def check(e):
    if x%2==0:
        print("even",end=" ")
    else:
        print("odd no",end=" ")

x = int(input("Enter no for verification : "))
if x<0:
    if x%2==0:
        print("even and -ve no")
    else:
        print("odd and -ve no")
elif x>0:
    check(x)
    print("+ve no")
elif x==0:
    check(x)
    print("zero")
else:
    pass


time.sleep(2)
os.system("clear")
