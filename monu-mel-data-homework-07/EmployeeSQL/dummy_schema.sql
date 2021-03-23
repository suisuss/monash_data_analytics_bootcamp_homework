employees
-
emp_no INT PK FK 
emp_title_id VARCHAR(30)
birth_date DATE
first_name VARCHAR(30)
last_name VARCHAR(30)
gender VARCHAR(10)
hire_date DATE
titles
-
emp_no INT FK >- employees.emp_no
title VARCHAR(30)


salaries
-
emp_no INT FK >- employees.emp_no
salary INT

dept_manager
-
dept_no VARCHAR(30) FK >- departments.dept_no
emp_no INT FK >- employees.emp_no

dept_emp
-
emp_no INT FK >- employees.emp_no
dept_no VARCHAR(30) FK >- departments.dept_no

departments
-
dept_no VARCHAR(30) PK 
dept_name VARCHAR(30)