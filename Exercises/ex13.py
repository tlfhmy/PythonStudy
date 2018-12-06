from sys import argv

script, first, second, third = argv


formatter = "Your {} variable is:{}"
print("The script is called:",script)
print(formatter.format("first",first))
print(formatter.format("second",second))
print(formatter.format("third",third))