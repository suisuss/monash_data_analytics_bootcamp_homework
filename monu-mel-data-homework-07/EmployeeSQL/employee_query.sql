-- 1. List the following details of each employee: employee number, last name, first name, sex, and salary.
SELECT e.emp_no, e.last_name, e.first_name, e.gender, s.salary
FROM employees e
FULL OUTER JOIN salaries s ON e.emp_no = s.emp_no
ORDER BY 1 ;


-- 2 .List first name, last name, and hire date for employees who were hired in 1986.
SELECT last_name, first_name, hire_date
FROM employees
WHERE hire_date BETWEEN '1986-01-01' AND '1986-12-31'
ORDER BY hire_date ASC;


-- 3. List the manager of each department with the following information: department number, department name,
-- the manager's employee number, last name, first name.
SELECT d.dept_no, d.dept_name, m.emp_no, e.last_name, e.first_name
FROM departments d
LEFT JOIN dept_manager m ON d.dept_no = m.dept_no
LEFT JOIN employees e ON e.emp_no = m.emp_no;

-- 4. List the department of each employee with the following information: employee number, last name, first name,
-- and department name.

SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM employees e
INNER JOIN dept_manager m ON
e.emp_no = m.emp_no
INNER JOIN departments d ON
m.dept_no = d.dept_no;

-- 5. List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."
SELECT first_name, last_name, gender
FROM employees
WHERE first_name LIKE 'Hercules' AND last_name LIKE 'B%';

-- 6. List all employees in the Sales department, including their employee number, last name, first name, and department name.
SELECT d_e.emp_no, e.last_name, e.first_name, d.dept_name
FROM employees e    
LEFT JOIN dept_emp d_e ON e.emp_no = d_e.emp_no
LEFT JOIN departments d ON d.dept_no = d_e.dept_no
WHERE dept_name LIKE 'Sales'
ORDER BY emp_no ASC;

-- 7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
SELECT d_e.emp_no, e.last_name, e.first_name, d.dept_name
FROM employees e      
LEFT JOIN dept_emp d_e ON e.emp_no = d_e.emp_no
LEFT JOIN departments d ON d.dept_no = d_e.dept_no
WHERE dept_name LIKE 'Sales' or dept_name LIKE 'Development'
ORDER BY dept_name desc;

-- 8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
SELECT last_name, COUNT(last_name)
FROM employees
GROUP BY last_name
ORDER BY last_name desc;