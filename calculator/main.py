while True:
    print("Select any choice: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Division")
    
    choice = int(input("Enter a choice: "))
    if choice > 0 and choice < 5:

        num1 = float(input("Enter 1st number: "))
        num2 = float(input("Enter 2nd number: "))
        
        if choice == 1:
            added_values = num1+num2
            print(added_values)
        elif choice == 2:
            sub_values = num1 - num2
            print(sub_values)
        elif choice == 3:
            multi_values = num1*num2
            print(multi_values)
        elif choice == 4:
            division_values = num1/num2
            print(division_values)
        else:
            print("Invalid Input ❌")
            break
    else:
        print("Invalid Input ❌")
        break