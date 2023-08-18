# File handling
path = input("Enter full file path: ")
with open(path) as file:
    print(file.read())

# If-elif-else
temp = float(input("Enter temperature in degrees celsius: "))
if temp < 0:
    print("Ice.")
elif temp > 100:
    print("Steam.")
else:
    print("Liquid.")

# Reverse string
string = input("Enter string to be reversed: ")
print(string[::-1])

# Vending Machine
item_price = float(input("Enter the item price in dollars ($): ")) * 100
amount_paid = float(input("Enter amount paid in dollars ($): ")) * 100
change = (amount_paid - item_price) / 100
print("Your change is ${:.2f}".format(change))

# Write to file, then read and print contents
with open("Lab4.txt", "w") as file:
    file.write("This is Lab 4, Activity 2, Question 3")
with open("Lab4.txt", "r") as file:
    print(file.read())

# Check string type
string = input("Enter string: ")
if string.isalpha():
    print("String contains only letters.")

    if string.isupper():
        print("String contains only uppercase letters.")
    elif string[0].isupper():
        print("String starts with an uppercase letter.")
    else:
        print("String contains only lowercase letters.")

elif string.isnumeric():
    print("String contains only digits.")

elif string.isalnum():
    print("String contains only letters and digits.")

elif string[0].isupper():
    print("String starts with an uppercase letter.")

elif string[-1] == ".":
    print("String ends with a period.")

else:
    pass

# Find min value
first = True
while True:
    num_value = float(input("Enter number value: "))

    if first == True:
        minimum = num_value
        first = False

    elif num_value < minimum:
        minimum = num_value

    else:
        break

print(minimum)

# Compare numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 == num2 == num3:
    print("All the same.")
elif num1 != num2 != num3:
    print("All different.")
else:
    print("Neither.")
