name = input("Enter your first and last name: ").split()
print(name[0][0], name[1][0])

volume = 6 * 350
print(volume)

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
print(
    "Sum: {}\nDifference: {}\nProduct: {}\nAverage: {}\nDistance: {}\nMaximum: {}".format(
        num1 + num2,
        num1 - num2,
        num1 * num2,
        (num1 + num2) / 2,
        abs(num1 - num2),
        max(num1, num2),
    )
)

meters = float(input("Enter length in meters: "))
print(
    "Miles: {:.2f}\nFeet: {:.2f}\nInches: {:.2f}".format(
        meters / 1609.3445, meters * 3.2808, meters * 39.3701
    )
)

drive = input("Enter drive letter: ")
path = input("Enter file path: ")
file_name = input("Enter file name: ")
extension = input("Enter file extension: ")
print(f"{drive}:{path}\{file_name}.{extension}")

# Variable name contains a function name which is bad practice

# Middle chars == " Y"
even_string = "Liu Yang"
# Middle char == "u"
odd_string = "Ian Gunther"
print(even_string[0])
print(even_string[-1])
# Middle char if len odd
print(odd_string[len(odd_string) // 2])
# Middle chars if len even
print(
    "{}{}".format(
        even_string[len(even_string) // 2 - 1], even_string[len(even_string) // 2]
    )
)
