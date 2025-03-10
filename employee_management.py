import json
import logging

# Configure logging
logging.basicConfig(filename='error_log.txt', level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []
        self.load_data()

    def load_data(self):
        """Load employees from a JSON file."""
        try:
            with open("employees.json", "r") as file:
                self.employees = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.employees = []  # If file not found or corrupt, start fresh
        except Exception as e:
            logging.error(f"Error loading data: {e}")

    def save_data(self):
        """Save employees to a JSON file."""
        try:
            with open("employees.json", "w") as file:
                json.dump(self.employees, file, indent=4)
        except Exception as e:
            logging.error(f"Error saving data: {e}")

    def add_employee(self, name, age, department, salary):
        """Add a new employee to the system."""
        try:
            employee = {
                "id": len(self.employees) + 1,
                "name": name,
                "age": int(age),
                "department": department,
                "salary": float(salary)
            }
            self.employees.append(employee)
            self.save_data()
            print(f"Employee {name} added successfully!")
        except ValueError:
            logging.error("Invalid input for age or salary")
            print("Error: Age must be an integer and salary a float.")
        except Exception as e:
            logging.error(f"Error adding employee: {e}")
            print("An error occurred while adding the employee.")

    def display_employees(self):
        """Display all employees."""
        if not self.employees:
            print("No employees found.")
        else:
            print("\nEmployee List:")
            for emp in self.employees:
                print(f"ID: {emp['id']}, Name: {emp['name']}, Age: {emp['age']}, "
                      f"Department: {emp['department']}, Salary: ${emp['salary']:.2f}")

    def search_employee(self, emp_id):
        """Search for an employee by ID."""
        try:
            emp_id = int(emp_id)
            for emp in self.employees:
                if emp["id"] == emp_id:
                    print(f"\nEmployee Found: {emp}")
                    return
            print("Employee not found.")
        except ValueError:
            logging.error("Invalid input for employee ID")
            print("Error: Employee ID must be an integer.")
        except Exception as e:
            logging.error(f"Error searching employee: {e}")
            print("An error occurred while searching for the employee.")

    def delete_employee(self, emp_id):
        """Delete an employee by ID."""
        try:
            emp_id = int(emp_id)
            for emp in self.employees:
                if emp["id"] == emp_id:
                    self.employees.remove(emp)
                    self.save_data()
                    print(f"Employee ID {emp_id} deleted successfully!")
                    return
            print("Employee not found.")
        except ValueError:
            logging.error("Invalid input for employee ID")
            print("Error: Employee ID must be an integer.")
        except Exception as e:
            logging.error(f"Error deleting employee: {e}")
            print("An error occurred while deleting the employee.")

if __name__ == "__main__":
    system = EmployeeManagementSystem()
    
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Search Employee by ID")
        print("4. Delete Employee by ID")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter name: ")
            age = input("Enter age: ")
            department = input("Enter department: ")
            salary = input("Enter salary: ")
            system.add_employee(name, age, department, salary)
        elif choice == "2":
            system.display_employees()
        elif choice == "3":
            emp_id = input("Enter employee ID: ")
            system.search_employee(emp_id)
        elif choice == "4":
            emp_id = input("Enter employee ID: ")
            system.delete_employee(emp_id)
        elif choice == "5":
            print("Exiting Employee Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
