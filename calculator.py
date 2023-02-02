def Addition(x,y):
    return (x+y)
def Subtraction(x,y):
    return (x-y)
def Multiplication(x,y):
    return (x*y)
def Division(x,y):
    return (x/y)

num_1 = int(input("Enter 1st number: "))
num_2 = int(input("Enter 2nd number: "))

print("Select Operation: ")
print("1.. Additon ")
print("2.. Subtraction ")
print("3.. Multiplication ")
print("4.. Division ")
print("5.. Exit code ")

while True:
    choice = int(input("Select 1/2/3/4/5: "))
    if choice in (1,2,3,4,5):
        if choice == 1:
            print("Addition: ", Addition(num_1, num_2))
        elif choice == 2:
            print("Subtraction: ", Subtraction(num_1, num_2))
        elif choice == 3:
            print("Multiplication: ", Multiplication(num_1, num_2))
        elif choice == 4:
            print("Division: ", Division(num_1, num_2))
        elif choice == 5:
            print("Thanks for your time")
            exit()
    else:
        print("Invalid Choice")