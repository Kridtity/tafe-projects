# math and random modules to calculate area of random circle diameter
from math import pi
import random

try:
    diameter = random.randint(1, 255)
    circle_area = pi * (diameter / 2) ** 2
    print("Diameter: " + str(diameter))
    print("Area: " + str(circle_area))

except Exception as e:
    print("Exception reached: " + str(e))


# import custom module and use built-in functions
import myMaths

num = input("Enter number: ")
choice = int(
    input(
        """Enter choice of function to apply to previous number:
                1 => Halve number
                2 => Double number
               Input: """
    )
)

if choice == 1:
    print(myMaths.halve_num(num))
elif choice == 2:
    print(myMaths.double_num(num))
else:
    print("Enter valid menu input.")


# use provided pizzas.py, add two pizzas, process customer order
from pizzas import pizzas

print("Pizza Menu:")
pizza_names = []
for dict in pizzas:
    pizza_names.append(dict["name"] + " pizza")
    print(pizza_names[-1])
    print("$" + str(dict["cost"]))
    print("Cheese: " + dict["cheese"])
    print("")

choice = input("Enter choice of pizza: ").lower()
payment_amount = float(input("Enter payment amount: "))

for name in pizza_names:
    if choice in name.lower():
        pizza = pizzas[(pizza_names.index(name))]
        print("Pizza choice: " + name)
        print("Cheese: " + pizza["cheese"])
        print("Cost: $" + str(pizza["cost"]))
        print("Change: $" + str(payment_amount - pizza["cost"]))

agreement = input("\nDo you agree with this order [Y/N]: ").upper()
if agreement == "Y":
    print("Transaction processed.")
else:
    print("Transactiuon cancelled.")
