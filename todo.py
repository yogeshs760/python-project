TODOS = []
print("""------TODOS APPlICATION------""")


while True:
    print("1. Add Task \n2. View Tasks \n3. Update \n4. Delete \n5. Exit \n6. Mark Completed")
    choice = input("Enter your choice: ")
    
    if choice == '1':           #-----Add Task
        task_id= input("Enter your id: ")
        task_name= input("Enter your task: ")
        is_completed= False
        TODOS.append({"ID":task_id,"Task":task_name,"is_completed":is_completed})

    elif choice == '2':         #-----Show All
        print("Your task: ", TODOS)  
        
    elif choice == '3':       #-----Update
        entered_id= input("Enter your id you want to update : ")
        # new_task= input("Enter your updated task : ")
        is_found=False
        for i in TODOS:
            if i["ID"]== entered_id:
                new_task= input("Enter your updated task : ")
                i["Task"]= new_task
                print('Task Updated Sucessfully')
                is_found=True
                break

        if is_found==False:
            print("ID not Found")
    
    elif choice == '4':       #-----Delete
        entered_id= input("Enter your id you want to delete : ")
        is_found=False
        for i in TODOS:
            if i["ID"]== entered_id:
                TODOS.remove(i)
                print('Task deleted Sucessfully')
                is_found=True
        if is_found==False:
            print("ID not Found")
    elif choice == '5':       #-----Exit
            print("exiciting todos ")
            break
    elif choice=='6':
        complete_id= input("Enter your id you want to show completed : ")
        is_found=False
        for item in TODOS:
            if item["ID"]== complete_id:
                item["is_completed"]= True
                print("Task mark changed")
                is_found=True
        if is_found==False:
            print("Not found")
    else:
        print("Invalid Choice")
