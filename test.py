print("Hello world")

print("Hello.")

name = input("Please enter your name: ")
print("Hello", name)

radius = input("Please enter a radius: ")
print(3.14 * float(radius) ** 2)

names = ["Pavlov", "Thorndike", "Skinner", "Little Albert"]
for i in names:
    print(i)

x = 0
for i in range(1, 11):
    x += i
print(x)

x = 1
for i in range(1, 11):
    x *= i
print(x)

print(
    """
    /////
   +\"\"\"\"\"+        
  (| 0 0 |)
   |  ^  |
   | '-' |
   +-----+
"""
)

print(3 * 4 + 5, 5 * 6 - 1)
