from Staff import Staff
from New_Employee import new_employee

staff = Staff()

def main():
    def add_new_employee(first_name, surname):
        staff.add_staff(new_employee(first_name, surname))
        main()
    def list_employees_emails():
        print([x.email for x in staff.staff])
        main()
    def list_employees():
        print([x.full_name for x in staff.staff])
        main()

    action = int(input("What would you like to do today? \n1 for add new employee; \n2 for list all existing employees; \n3 for list all existing employees emails;\n"))
    if action == 1:
        given_names = input("Enter First Name: ")
        forenames = input("Enter Surname: ")
        add_new_employee(given_names, forenames)
    elif action == 2:
        list_employees()
    else:
        list_employees_emails()

main()
