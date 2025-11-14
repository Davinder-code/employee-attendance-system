CREATE DATABASE attendance_system;
USE attendance_system;
CREATE TABLE departments (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    department_name VARCHAR(100) NOT NULL
);
CREATE TABLE employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    department_id INT,
    hire_date DATE,
    status VARCHAR(20) DEFAULT 'Active',
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);
CREATE TABLE attendance (
    attendance_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_id INT,
    date DATE,
    clock_in TIME,
    clock_out TIME,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
);
INSERT INTO departments (department_name) VALUES
('HR'),
('IT'),
('Finance'),
('Marketing');
INSERT INTO employees (first_name, last_name, email, phone, department_id, hire_date)
VALUES
('John', 'Doe', 'john.doe@example.com', '555-1010', 2, '2023-01-15'),
('Anna', 'Smith', 'anna.smith@example.com', '555-2020', 1, '2024-03-10'),
('David', 'Singh', 'david.singh@example.com', '555-3030', 4, '2022-11-20');
INSERT INTO attendance (emp_id, date, clock_in, clock_out) VALUES
(1, '2025-11-10', '09:00:00', '17:30:00'),
(1, '2025-11-11', '09:10:00', '17:15:00'),

(2, '2025-11-10', '08:50:00', '17:05:00'),
(2, '2025-11-11', '09:00:00', '17:00:00'),

(3, '2025-11-10', '09:05:00', '17:45:00');
SELECT e.emp_id, e.first_name, e.last_name, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id;
SELECT e.first_name, e.last_name, a.date, a.clock_in, a.clock_out
FROM attendance a
JOIN employees e ON a.emp_id = e.emp_id
ORDER BY a.date, e.emp_id;
SELECT emp_id, date,
TIMEDIFF(clock_out, clock_in) AS hours_worked
FROM attendance;
SELECT emp_id,
       COUNT(date) AS days_present
FROM attendance
WHERE MONTH(date) = 11 AND YEAR(date) = 2025
GROUP BY emp_id;
SELECT emp_id, first_name, last_name
FROM employees
WHERE emp_id NOT IN (
    SELECT emp_id FROM attendance WHERE date = '2025-11-11'
);
