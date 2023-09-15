"""# Copy program to correct errors and determine function
a = 0
b = 5


def main():
    global a, b
    i = 10
    b = g(i)
    print(a + b + i)


def f(i):
    n = 0
    while n * n <= i:
        n = n + 1
    return n - 1


def g(a):
    b = 0
    for n in range(a):
        i = f(n)
        b = b + i
    return b


main()


# Use recursion to determine number of digits in integer n
n = input("Enter number to determine number of digits: ")

n_length = 0
for i in n:
    n_length += 1

print("Number of digits in input number: {}".format(n_length))


# Digit finder thing (first digit, last digit, number of digits)
def main():
    number = str(
        int(
            input(
                "Enter integer to determine first digit, last digit, and number of digits: "
            )
        )
    )
    firstDigit(number)
    lastDigit(number)
    digits(number)


def firstDigit(n):
    print("First digit: " + n[0])


def lastDigit(n):
    print("Last digit: " + n[-1])


def digits(n):
    print("Number of digits: " + str(len(n)))


main()


# Convert Roman numerals into decimal integers
def main():
    roman = input("Enter Roman numeral string: ")
    roman_to_dec(roman)


def roman_to_dec(roman):
    vals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    roman = list(roman.upper())

    dec = 0
    for i in roman:
        dec += vals[i]

    print("Decimal equivalent: " + str(dec))


main()"""


# Find match in string using recursion
def main():
    string = input("Enter string: ")
    regex = input("Enter expression to find in string: ")

    print("Expression found: " + str(find(string, regex)))


def find(string, regex):
    if len(regex) <= len(string):
        for i in range(len(string)):
            if regex == string[: (len(regex) + 1)]:
                return True
            else:
                string = string[1:]
        return False
    else:
        return False


main()
