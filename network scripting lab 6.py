# Compute volume of two cubes
def main():
    for i in range(2):
        total_volume = 0
        side_length = float(input("Enter float length of cube side: "))
        print(
            "Cube volume for cube with side length {} is: {} units^3".format(
                side_length, cubeVolume(side_length)
            )
        )

        total_volume += cubeVolume(side_length)

    print(total_volume)


def cubeVolume(side_length):
    return side_length**3


main()


# Write function to find smallest of three and another to find average of three and test
def smallest(x, y, z):
    smallest_num = min([x, y, z])
    return smallest_num


def average(x, y, z):
    avg = sum([x, y, z]) / len([x, y, z])
    return avg


x = float(input("Enter float 1: "))
y = float(input("Enter float 2: "))
z = float(input("Enter float 3: "))

print(smallest(x, y, z), average(x, y, z))


# Return middle of string
def middle(string):
    if len(string) % 2 == 0:
        return "{}{}".format(string[len(string) // 2 - 1], string[len(string) // 2])
    else:
        return string[len(string) // 2]


print(middle(input("Enter string: ")))


# Volume functions
import math


def sphereVolume(r):
    volume = 4 / 3 * math.pi * r**3
    return volume


def sphereSurface(r):
    sa = 4 * math.pi * r**2
    return sa


def cylinderVolume(r, h):
    volume = math.pi * r**2 * h
    return volume


def cylinderSurface(r, h):
    sa = 2 * math.pi * r * h + 2 * math.pi * r**2
    return sa


def coneVolume(r, h):
    volume = math.pi * r**2 * (h / 3)


def coneSurface(r, h):
    sa = math.pi * r * (r + math.sqrt(h**2 + r**2))
    return sa


# Coffee making instructions
# CBB doing so I'll leave it
