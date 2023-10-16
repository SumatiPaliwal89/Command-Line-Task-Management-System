import pickle

class Task:
    def __init__(self, title, description, status="Incomplete"):
        self.title = title
        self.description = description
        self.status= status
        
def add(tasks):
    title=input("Enter the task title: ")
    description=input("Enter the task description: ")
    t=Task(title,description)
    tasks.append(t)
    print("Task Added Successfully")
    
def display(tasks):
    if tasks==[]:
        print("No Task Found")
    else:
        print("\n TASKS  \n")
        for i in tasks:
            print("\nTask title: ",i.title,"\nTask description: ",i.description,"\nCompletion status: ",i.status) 

def completed(tasks):
    flag=7
    if tasks==[]:
        print("No tasks")
    else:
        comp=input("Enter the title of task to mark complete: ")
        for i in tasks:
            if i.title==comp:
                i.status="Complete"
                print("Task marked as completed successfully")
                display(tasks)
                flag=8
        if flag==7:
            print("Task not found")
        
def delete(tasks):
    flag=7
    if tasks==[]:
        print("No tasks")
    else:
        tdel=input("Enter the title of task to delete: ")
        for i in range(len(tasks)):
            if tasks[i].title==tdel:
                a=i
                flag=8
        if flag==7:
            print("Task not found")
        else:
            d=tasks.pop(a)
            print("Task ",d.title," deleted successfully")
            display(tasks)

def save(tasks,file):
    with open(file,"wb") as f:
        pickle.dump(tasks,f)
        print("Tasks Saved Succesfully")

def load(fname):
    try:
        with open(fname,"rb") as f:
            data=pickle.load(f)
            print(display(data))
    except FileNotFoundError:
        print("File not found")

def menu():
    tasks=[]
    while True:
        print("\n MENU  \n")
        print("1. Add a new task")
        print("2. Display all tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Save tasks to a file")
        print("6. Load tasks from a file")
        print("7. Quit the program")
    
        ch=input("\nEnter your choice: ")
        if ch=="1":
            add(tasks)
        elif ch=="2":
            display(tasks)
        elif ch=="3":
            completed(tasks)
        elif ch=="4":
            delete(tasks)
        elif ch=="5":
            file=input("Enter the file name to save tasks into: ")
            save(tasks,file)
        elif ch=="6":
            fname=input("Enter the file name to load tasks from: ")
            tasks = load(fname)
        elif ch=="7":
            break
        else:
            print("Please enter valid choice")
menu()
