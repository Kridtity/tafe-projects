# try and except blocks to determine area of a circle
import math

try:
    radius = float(input("Enter circle radius to calculate circle area: "))
    circle_area = math.pi * radius**2
    print("Circle area: {} unit**2".format(circle_area))
except BaseException as e:
    print("The program ran into an error: " + str(e))


# try and except blocks used in receiving user input password between 8 and 16 characters
try:
    password = input("Enter password of length between 8 and 16: ")
    assert (
        len(password) > 8
    ), "Invalid input (password less than or equal to eight (8) characters long)"
    assert (
        len(password) < 16
    ), "Invalid input (password greater than or equal to sixteen (16) characters long)"
    print("Password accepted.")
except BaseException as e:
    print("The program ran into an error: " + str(e))


# add digits together from a single string delimited by spaces
try:
    numbers = input(
        "Enter list of numbers to be added together, each separated by a single space: "
    ).split()

    sum = 0
    for number in numbers:
        sum += float(number)

    print("The sum is: " + sum)

except ValueError as e:
    print("The program ran into an error: " + str(e))


# simple (and garbage) text file editor
menu_input = input(
    """
    Garbage Text Editor v0.0.69
      Menu:
      1 => Create file
      2 => Edit file
      3 => Read file
      4 => Exit file

      """
)

if menu_input == "1":
    print("Creating file")
    file_name = input("Enter file name: ") + ".txt"

    try:
        with open(file_name, "x") as file:
            file.write(
                input("Enter file text to be written and press enter to save:\n")
            )
    except FileExistsError as e:
        print("Error creating file: " + str(e))

elif menu_input == "2":
    print("Editing file")
    print("*Note: append only\n")
    file_name = input("Enter file name: ") + ".txt"

    try:
        with open(file_name, "a") as file:
            file.write(
                input("Enter file text to be written and press enter to save:\n")
            )
    except FileNotFoundError as e:
        print("Error opening file: " + str(e))

elif menu_input == "3":
    print("Reading file")
    file_name = input("Enter file name: ") + ".txt"

    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line)

    except FileNotFoundError as e:
        print("Error reading file: " + str(e))

elif menu_input == "4":
    pass
else:
    print("Ya donkey.")
