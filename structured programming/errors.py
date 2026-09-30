try:
    a=int(input("First number:"))
    b = int(input("Second number:"))
    print("Results:" , a / b)
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

while True:
    try:
        age = int(input("enter your age:"))
        break      #leave the loop if conversion worked
    except ValueError:
        print("please Enter a whole number:")
print("age recorded:", age)
