def print_two(*args):
    arg1, arg2 = args
    print(f"arg1:{arg1},arg2:{arg2}")

def print_two_again(arg1,arg2):
    print(f"arg1:{arg1},arg2:{arg2}")

def print_one(arg1):
    print(f"arg1:{arg1}")

def print_non():
    print("I got nothing.")

print_two("pr1","pr2")

print_two_again("pr1a","pr2a")

print_one("prone")

print_non()
