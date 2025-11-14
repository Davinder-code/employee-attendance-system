# employees.py

from database import get_connection
from datetime import date

# 🔹 Converts department name → ID
def get_department_id(dept_name):
    dept_name = dept_name.strip().lower()

    mapping = {
        "hr": 1,
        "it": 2,
        "finance": 3,
        "marketing": 4
    }

    return mapping.get(dept_name, None)


def add_employee(first, last, email, phone, dept_name):
    dept_id = get_department_id(dept_name)

    if dept_id is None:
        print("❌ Invalid department name! Use: HR, IT, Finance, Marketing")
        return

    db = get_connection()
    cursor = db.cursor()

    query = """
    INSERT INTO employees (first_name, last_name, email, phone, department_id, hire_date)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    cursor.execute(query, (first, last, email, phone, dept_id, date.today()))
    db.commit()

    print("✅ Employee added successfully!")

    cursor.close()
    db.close()


def list_employees():
    db = get_connection()
    cursor = db.cursor()

    cursor.execute("SELECT emp_id, first_name, last_name FROM employees")
    rows = cursor.fetchall()

    print("\n--- Employee List ---")
    for row in rows:
        print(f"ID: {row[0]}  |  {row[1]} {row[2]}")

    cursor.close()
    db.close()
