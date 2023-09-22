# Not my code, provided by course for development of testing plan purposes
"""
You must create a gradebook program which inputs four grades
for a student, calculates the average, and advises of their final grade.
"""

mark_1 = int(input("Please enter first grade: "))
mark_2 = int(input("Please enter first grade: "))
mark_3 = int(input("Please enter first grade: "))
mark_4 = int(input("Please enter first grade: "))

mark_average = (mark_1 + mark_2 + mark_3 + mark_4) / 4

if mark_average > 93 and mark_average < 100:
    print("The student received an A.")
if mark_average > 85 and mark_average < 92:
    print("The student received a B.")
if mark_average > 77 and mark_average < 84:
    print("The student received a C.")
if mark_average > 70 and mark_average < 76:
    print("The student received a D")
else:
    print("The student received an F")


# Not my code, provided by course for debugging purposes
"""
This code will take a value and convert it into multiple types.
"""

varValue = "1.0"
print(varValue)
print("Turning varValue into a float")
varValue = float(varValue)
print(varValue)
print("Turning varValue into a integer")
varValue = int(varValue)
print(varValue)
print("Turning varValue into a back into a string")
varValue = str(varValue)
print(varValue)
print("Turning varValue into a list")
varValue = list(varValue)
print(varValue)
print("All done!")
