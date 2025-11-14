# main.py

from instructions import show_menu
from attendance import clock_in, clock_out
from employees import add_employee, list_employees

while True:
    show_menu()
    choice = input("Choose option: ")

    if choice == "1":
        emp_id = int(input("Enter Employee ID: "))
        clock_in(emp_id)

    elif choice == "2":
        emp_id = int(input("Enter Employee ID: "))
        clock_out(emp_id)

    elif choice == "3":
      print("\n--- Add New Employee ---")
      first = input("First Name: ")
      last = input("Last Name: ")
      email = input("Email: ")
      phone = input("Phone: ")
      dept = input("Department Name (HR / IT / Finance / Marketing): ")

      add_employee(first, last, email, phone, dept)


    elif choice == "4":
        list_employees()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid option, try again.")
