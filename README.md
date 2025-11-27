#Employee Attendance Management System (Python + MySQL)

A professional, multi-file **Employee Attendance System** built using **Python** and **MySQL** to manage employee records and track daily attendance (Clock In / Clock Out).  
This project follows a clean, modular, real-world architecture suitable for resumes, GitHub portfolios, and college projects.

---

##Features

###Employee Management
- Add new employees  
- Stores name, email, phone, department, hire date  
- Data saved securely in MySQL  

### Attendance Tracking
- Clock In  
- Clock Out  
- Prevents duplicate clock-ins  
- Stores timestamps accurately  
- Uses foreign-key constraints for reliability  

###Clean Modular Architecture

```
attendance_system/
│
├── main.py
├── attendance.py
├── employees.py
├── instructions.py
├── database.py
└── config.py
```

### Database Structure
Uses MySQL with tables:
- `employees`
- `departments`
- `attendance`

---

## Technologies Used

- Python 3  
- MySQL  
- mysql-connector-python  
- Modular programming  
- Foreign-key database design  

---

## Folder Structure

```
attendance_system/
│
├── main.py                # Main program (menu handler)
├── attendance.py          # Clock-in / Clock-out functions
├── employees.py           # Add employee, list employees
├── database.py            # MySQL connection helper
├── instructions.py        # Displays menu to the user
└── config.py              # MySQL credentials
```

---

##How to Run the Project

### Install Dependencies
```bash
pip install mysql-connector-python
```

---

###Create the MySQL Database

Run in MySQL Workbench:

```sql
CREATE DATABASE attendance_system;
```

Insert default departments:

```sql
INSERT INTO departments (department_name) VALUES
('HR'), ('IT'), ('Finance'), ('Marketing');
```

---

###Configure Database Credentials

Edit `config.py`:

```python
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "your_mysql_password"
DB_NAME = "attendance_system"
```

---

###Run the Application
```bash
python main.py
```

---

##Application Menu

```
--- Employee Attendance System ---
1. Clock In
2. Clock Out
3. Add New Employee
4. Show Employee List
5. Exit
```

---

##Future Improvements
- GUI Version (Tkinter)  
- Admin Login System  
- Export Attendance to Excel  
- Web Dashboard (Flask/Django)  
- Late/Early attendance reports  
- Auto-generate monthly summaries  

---

##Contributions
Pull requests are welcome!  
For major changes, please open an issue first.

---

## License
This project is free for personal and educational use.
