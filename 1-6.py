#1.
print("E.Muthulakshmi")
print("JRA, Department of physics")
print("SSN College of engineering")
print("kalavakkam,chennai-603 110.")
#2.
your_name=input("What's your name?")
print("Hello  "+ your_name)
#3 & 4.
square_feet=43560
length=int(input("Enter the length of the room:"))
width=int(input("Enter the width of the room:"))
area=length*width
area_of_field=length*width/square_feet
print(f"The area of the room in square feet: {area} ")
print(f"Area of the field in acres: {area_of_field}")
#5.
less_deposit=0.10
more_deposit=0.25
a=int(input("No.of containers having one litre or less: "))
b=int(input("No.of containers have more than one litre: "))
refund=a*less_deposit+b*more_deposit
print(f"refund will be $ {refund}")
#6.
tax=0.05
tip=0.18
Meal_cost=float(input("Enter the cost of the meal: "))
a=Meal_cost*tax
b=Meal_cost*tip
Total_amount=a+b+Meal_cost
print(f"Tax:Tip:Total amount:{a}:{b}:{Total_amount}")
