from employee import Employeefunc
from file_handler import FileManager
from exception import EmployeeManagementException

def display_menu():
    print("Employee Management System")
    print("1. Add New Employee")
    print("2. Display Employee Details")
    print("3. Save Employee Data to File")
    print("4. Retrieve Employee Data from File")
    print("5. Exit")

def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_employee_details():
    name = input("Enter employee name: ")
    age = get_int_input("Enter employee age: ")
    designation = input("Enter employee designation: ")
    return Employeefunc(name, age, designation)

def add_employee(employees):
    employee = get_employee_details()
    employees.append(employee)
    print("Employee added successfully!")

def display_employee_details(employees):
    if len(employees) == 0:
        print("No employees found.")
    else:
        for index, employee in enumerate(employees, start=1):
            print(f"\nEmployee {index}:")
            print("Name:", employee.name)
            print("Age:", employee.age)
            print("Designation:", employee.designation)

def save_employee_data(employees):
    file_name = input("Enter the file name to save employee data: ")
    try:
        FileManager.create_file(file_name)
        FileManager.write_data(file_name, employees)
        print("Employee data saved successfully!")
    except EmployeeManagementException as e:
        print("Error:", str(e))

def retrieve_employee_data():
    file_name = input("Enter the file name to retrieve employee data: ")
    try:
        data = FileManager.read_data(file_name)
        return data
    except EmployeeManagementException as e:
        print("Error:", str(e))
        return []

def main():
    employees = []
    while True:
        display_menu()
        choice = get_int_input("Enter your choice (1-5): ")
        if choice == 1:
            add_employee(employees)
        elif choice == 2:
            display_employee_details(employees)
        elif choice == 3:
            save_employee_data(employees)
        elif choice == 4:
            employees = retrieve_employee_data()
        elif choice == 5:
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
