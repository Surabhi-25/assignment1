from employee import Employeefunc
class FileManager:
    @staticmethod
    def create_file(file_name):
        try:
            with open(file_name, 'w'):
                pass
        except IOError:
            raise EmployeeManagementException("Error creating file.")

    @staticmethod
    def write_data(file_name, employees):
        try:
            with open(file_name, 'w') as file:
                for employee in employees:
                    file.write(f"{employee.name},{employee.age},{employee.designation}\n")
        except IOError:
            raise EmployeeManagementException("Error writing data to file.")

    @staticmethod
    def read_data(file_name):
        try:
            employees = []
            with open(file_name, 'r') as file:
                for line in file:
                    name, age, designation = line.strip().split(",")
                    employee = Employeefunc(name, int(age), designation)
                    employees.append(employee)
            return employees
        except IOError:
            raise EmployeeManagementException("Error reading data from file.")
