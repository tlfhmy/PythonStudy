from sys import argv

script, input_file = argv

def print_all(flna):
    print(flna.read())

def print_line(line,flna):
    print(line,flna.readline())

filename = open(input_file)

print("Let's print the whole file:\n")

print_all(filename)

print("Now print every line.\n")

filename.seek(0)

line = 1
print_line(line,filename)

line += 1
print_line(line,filename)

line += 1
print_line(line,filename)

