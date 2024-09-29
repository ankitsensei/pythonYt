def Tasks(allTask):
    for i in range(len(allTask)):
        print(f"{i+1}. {allTask[i]}")


allTask = ['Math hw', 'Physics assignment', 'chemistry hw']
while True:
    print("🔴 Select one of the following options:-")
    print('''
        1. Add a task
        2. Delete a task
        3. View all task
        4. Exit
        ''')
    
    
    user = int(input(": "))
    
    if user ==  1:
        addTask = input("Enter a task: ")
        allTask.append(addTask)
        Tasks(allTask)
    elif user == 2:
        Tasks(allTask)
        deleteTask = int(input("Enter serial no.: ")) - 1
        del allTask[deleteTask]
        Tasks(allTask)
    elif user == 3:
        Tasks(allTask)
    else:
        break