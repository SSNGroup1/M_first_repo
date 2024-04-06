Ex:37
sides=int(input("Enter the no.of sides: "))
shape=" "
if sides==3:
    shape="traingle"
elif sides==4:
    shape="Quadrilateral"
elif sides==5:
    shape="Pentagon"
elif sides==6:
    shape="Hexagon"
elif sides==7:
    shape="Heptagon"
elif sides==8:
    shape="Octagon"
elif sides==9:
    shape="Nonagon"
elif sides==10:
    shape="Decagon"
if shape == "":
    print("Error")
else:
    print(shape)
Ex:38
month=str(input("Enter the month: "))
if month=="april" or month=="june" or month=="september" or month=="november":
    print(month,"has","30")
elif month=="february":
    print( month,"has","28 or 29")
else:
    print(month,"has","31")
 Ex:39
s1=int(input("Enter traingle side1:"))
s2=int(input("Enter traingle side2:"))
s3=int(input("Enter traingle sise3:"))
if s1==s2 and s2==s3:
    print("Traingle: Equilateral")
elif s1==s2 or s2==s3 or s3==s1:
    print("Traingle: isoceles")
else:
    print("Traingle: scalene")
#Ex:40
c4=261.63
d4=293.66
e4=329.63
f4=349.23
g4=392.00
a=440.00
b4=493.88
limit=1
freq=int(input("Enter a frequency:  ")
if freq>=C4-limit and freq<=c4+limit :
    note="c4"
if freq>=d4-limit and freq<=d4+limit :
    note="d4"
if freq>=e4-limit and freq<=e4+limit :
    note="e4"
if freq>=g4-limit and freq<=g4+limit :
    note="g4"
if freq>=a4-limit and freq<=a4+limit :
    note="a4"
if freq>=b4-limit and freq<=b4+limit :
    note="b4"
else:
    note=" "
Ex:41
raise_Factor=2400.00
unacceptable=0
acceptable=0.4
meritorious=0.6
rating=float(input("Enter the rating:"))
if rating==unacceptable:
    performance="unacceptable"
elif rating==acceptable:
    performance="Acceptable"
elif rating >=meritorious:
    performance="Meritorious" 
else:
    performance=" "
if performance==" ":
    print("Not valid rating")
else:
    print("The performance is",performance,rating*raise_Factor)
