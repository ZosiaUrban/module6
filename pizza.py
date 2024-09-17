import math


diameter=int(input("Enter the diameter of the pizza: "))
price=int(input("Enter the price of the pizza: "))


def unitcalculator(diameter, price):
      radius=diameter/2
      area=math.pi*radius**2
      totalvalperinch= price / area
      return totalvalperinch



totalvalperinch=unitcalculator(diameter,price)
print("the value per inch is" ,totalvalperinch)



