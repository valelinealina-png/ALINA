#


marks = []
n = int(input("how many marks?"))

for i in range(n):
    value = int(input("enter mark:"))
    marks.append(value)

if len(marks) > 0:
    average = sum(marks)/ len(marks)
    print("average:", average)
    print("highest:", max(marks))
    print("lowest:", min(marks))
else:
    print("no marks entered")



    while True:
        print("\n1. Add")
        print("2. View")
        print("3. Exit")

        choice = input("choose an option: ")
        match choice:
            case "1":
                print("add selected")
            case "2":
                print("view selected")
            case "3":
                print("goodbye")
                break
            case _:
                print("invalid choice")
