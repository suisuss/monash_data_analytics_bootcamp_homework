DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS dept_emp;
DROP TABLE IF EXISTS dept_manager;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS salaries;
DROP TABLE IF EXISTS titles;


-- CREATE TABLES
CREATE TABLE "employees" (
    "emp_no" INT   NOT NULL,
    "emp_title_id" VARCHAR(30) NOT NULL,
    "birth_date" VARCHAR(10) NOT NULL,
    "first_name" VARCHAR(30)   NOT NULL,
    "last_name" VARCHAR(30)   NOT NULL,
    "gender" VARCHAR(10)   NOT NULL,
    "hire_date" VARCHAR(10) NOT NULL,
    CONSTRAINT "pk_employees" PRIMARY KEY (
        "emp_no"
        )
);

CREATE TABLE "titles" (
    "title_id" VARCHAR(30)   NOT NULL UNIQUE,
    "title" VARCHAR(30)   NOT NULL
);


CREATE TABLE "salaries" (
    "emp_no" INT   NOT NULL,
    "salary" INT   NOT NULL
);


CREATE TABLE "dept_emp" (
    "emp_no" INT   NOT NULL,
    "dept_no" VARCHAR(30)   NOT NULL
);

CREATE TABLE "dept_manager" (
    "dept_no" VARCHAR(30)   NOT NULL,
    "emp_no" INT NOT NULL
);

CREATE TABLE "departments" (
    "dept_no" VARCHAR(30)   NOT NULL,
    "dept_name" VARCHAR(30)   NOT NULL,
    CONSTRAINT "pk_departments" PRIMARY KEY (
        "dept_no"
     )
);

-- CREATE FOREIGN KEYS
ALTER TABLE "titles" ADD CONSTRAINT "titles-emp_title-FK" FOREIGN KEY("emp_title")
REFERENCES "employees" ("emp_title");

ALTER TABLE "salaries" ADD CONSTRAINT "salaries-emp_no-FK" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

ALTER TABLE "dept_emp" ADD CONSTRAINT "dept_emp-emp_no-FK" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

ALTER TABLE "dept_emp" ADD CONSTRAINT "dept_emp-dept_no-FK" FOREIGN KEY("dept_no")
REFERENCES "departments" ("dept_no");

ALTER TABLE "dept_manager" ADD CONSTRAINT "dept_manager-dept_no-FK" FOREIGN KEY("dept_no")
REFERENCES "departments" ("dept_no");

ALTER TABLE "dept_manager" ADD CONSTRAINT "dept_manager-emp_no-FK" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");


