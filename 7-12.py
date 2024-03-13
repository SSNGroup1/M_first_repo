#7.
n=int(input("Enter the integer n: "))
a=n*(n+1)/2
print("The sum of positive integer is",a)

#8.
widget_weighs=75
gizmos_weighs=112
Weight=int(input("Enter the no.of Widget: "))
Gizmos=int(input("Enter the no.of Gizmos: "))
a=Weight*widget_weighs
b=Gizmos*gizmos_weighs
print("Total weight of the order=",a+b,"grams")

#9.
Deposit=int(input("Enter the Deposit amount :"))
interest=int(input("Enter the interest rate:"))  
s1=((Deposit*interest)/100)+Deposit
s2=(s1*interest/100)+s1
s3=(s2*interest/100)+s2
print(f"Deposite amount={Deposit},1year={s1},2nd year={s2},3rd year={s3}")

#10.
import math      
a=int(input("Enter the value 1:"))
b=int(input("Enter the value 2: "))
print("a+b:",a+b)
print("a-b:",a-b)
print("a*b:",a*b)
print("a/b:",a/b)
print("a%b:",a % b)
print("log10(a):",math.log10(a))

#11.
america= int(input("Enter the fuel efficiency:"{}"MPG"))
canada=america*235.215
print(canada,"L/100km")

#12.
from math import sin,cos
t1=0.3
t2=0.4
g1=0.5
g2=0.6
a=6371.01*(sin(t1)*sin(t2)+cos(t1)*cos(t2)*cos(g1-g2))
print(a)






