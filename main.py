#Phase 1 EmployManagement
import json

emp_db = {}
Employ_file = "E:\Linked in _ Future Goal\EmployManagement\employ_data.json"

try:
    with open(Employ_file,"r") as f:
        data=json.load(f)
    emp_db = {int(k): v for k, v in data.items()}
except ( json.JSONDecodeError,FileNotFoundError):
    emp_db = {}
    


def save_data():
    with open(Employ_file,'w') as file:
        json.dump(emp_db,file)

def add():
    eid = int(input("Enter Employee Id: "))
    if(eid in emp_db):
        print("Employer Id Already Present")
        return
    ename = input("Employer Name: ")
    erole = input("Employer Role:")
    salary = int(input("Employer Salary:"))

    emp_db[eid] = {"Name":ename,"Role":erole,"salary":salary}
    if emp_db:
        save_data()
    else:
        print("Employee Data Empty")



def view():
    print("1. View All Employees\n2. Search by ID\n3. Search by Name")
    ch = int(input("Enter Choice: "))
    
    if ch == 1:
        for index, eid in enumerate(emp_db, start=1):
            emp = emp_db[eid]
            print(f"{index}. ID: {eid}, Name: {emp['Name']}, Role: {emp['Role']}, Salary: {emp['salary']}")
    
    elif ch == 2:
        eid = int(input("Enter ID: "))
        if eid in emp_db:
            emp = emp_db[eid]
            print(f"ID: {eid}, Name: {emp['Name']}, Role: {emp['Role']}, Salary: {emp['salary']}")
        else:
            print("Wrong Employee ID")
    
    elif ch == 3:
        name = input("Enter Name: ")
        found = False
        for eid, emp in emp_db.items():
            if emp['Name'].lower() == name.lower():
                print(f"ID: {eid}, Name: {emp['Name']}, Role: {emp['Role']}, Salary: {emp['salary']}")
                found = True
        if not found:
            print("Wrong Employee Name")

   
def remove():
    id = int(input("Enter the Remove Id: "))
    if(id in emp_db):
        confirm = int(input("Are You Sure[1/0]:"))
        if(confirm == 1):    
            delete =  emp_db[id]
            del emp_db[id]
            save_data()
            print("Deleted ID: ",delete)
    else:
        print("Wrong Id ")

def main_menu():
    print("\n--- Employee Management System ---")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Remove Employee")
    print("4. Exit")


while True:
    main_menu()
    try:
        choice = int(input("Enter the Choice:"))
    except ValueError:
          print("Enter Only Number")
          continue
          

    if(choice == 1):
        add()
    if(choice == 2):
        view()
    if(choice == 3):
        remove()
    if(choice == 4):
        break

    


