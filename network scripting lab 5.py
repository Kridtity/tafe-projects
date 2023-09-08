# Compute min and max of list until exit
receive_input = True
int_list = []
while receive_input == True:
    new_int = int(input("Enter an integer: "))
    int_list.append(new_int)

    loop_bool = input("Continue? [Y/N]: ").lower()

    if not (loop_bool == "y" or loop_bool == "yes"):
        receive_input = False

    int_list.sort()
    print("Maximum: {}\nMinimum: {}".format(int_list[-1], int_list[0]))
print("")

# Read 10 numbers then sort and print in reverse order of input
num_list = []
for i in range(10):
    new_num = int(input("Enter an integer: "))
    num_list.append(new_num)

n = -1
for i in num_list:
    print(num_list[n])
    n -= 1

# Sort by length
num_strings = int(input("Enter number of strings to be input: "))
string_list = []
for i in range(num_strings):
    string_list.append(input("Enter string: "))

string_list.sort(key=len)
print(string_list)

# Sort 2D lists by decreasing order
continent_list = [
    {"continent": "Africa", "population": 1766},
    {"continent": "Asia", "population": 5268},
    {"continent": "Australia", "population": 46},
    {"continent": "Europe", "population": 628},
    {"continent": "North America", "population": 392},
    {"continent": "South America", "population": 809},
]

continent_list.sort(reverse=True, key=lambda x: x[1])
print(continent_list)

# 10 random numbers between 1 and 100
import random

rand_int_list = []
for i in range(10):
    rand_int_list.append(random.randint(1, 100))

print(rand_int_list)

# Read text file, search for lowercase chars, print all words containing the char in alphabetical order for all letters of the alphabet, build dict with lowercase chars as keys and words containing the letters in a set as values
import string

with open("sample_text.txt", "r") as file:
    file_text = file.read().lower().split()

alphabet = list(string.ascii_lowercase)
final_words_list = []

for letter in alphabet:
    temp_word_list = []
    print("Current letter: {}".format(letter))
    for word in file_text:
        if letter in word:
            temp_word_list.append(word)

    print(temp_word_list)
    final_words_list.append(temp_word_list)

words_dict = dict(zip(alphabet, final_words_list))

# Print data in tabular format
title_format = "\n+{0:^98}+"
title = "Population Per Continent (in millions)"
header = ["Year", 1750, 1800, 1850, 1900, 1950, 2000, 2050, "Total Growth"]
africa = ["Africa", 106, 107, 111, 133, 221, 767, 1766]
asia = ["Asia", 502, 635, 809, 947, 1402, 3634, 5268]
australia = ["Australia", 2, 2, 2, 6, 13, 30, 46]
europe = ["Europe", 163, 203, 276, 408, 547, 729, 628]
north_america = ["North America", 2, 7, 26, 82, 172, 307, 392]
south_america = ["South America", 16, 24, 38, 74, 167, 511, 809]
row_separator = "├---------------+---------+---------+---------+---------+---------+---------+---------+------------┤"
column_separator = "|{0:15}|{1:9}|{2:9}|{3:9}|{4:9}|{5:9}|{6:9}|{7:9}|{8:12}|"

continents = africa, asia, australia, europe, north_america, south_america
row_data = header, africa, asia, australia, europe, north_america, south_america

for continent in continents:
    continent.append(continent[-1] - continent[1])

# Print table
print(title_format.format(title))
for row in row_data:
    print(
        column_separator.format(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]
        )
    )
    print(row_separator)
