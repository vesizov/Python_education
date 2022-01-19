-- CREATE TABLE students(

-- 	First_name TEXT,
-- 	Last_name TEXT,
-- 	Age INTEGER

-- );

-- CREATE TABLE employees(

-- 	First_name TEXT,
-- 	Last_name TEXT,
-- 	Age INTEGER
-- );

-- .tables

-- SELECT * FROM students;


-- CRUD -- CREATE, READ, UPDATE, DELETE

-- INSERT INTO students (First_name, Last_name, Age) VALUES ('Jack', 'White', 18);
-- INSERT INTO students (First_name, Last_name, Age) VALUES ('Jane', 'Black', 19);

-- INSERT INTO employees (First_name, Last_name, Age) VALUES ('Jack', 'White', 18);
-- INSERT INTO employees (First_name, Last_name, Age) VALUES ('Jane', 'Black', 19);
-- INSERT INTO employees (First_name, Last_name, Age) VALUES ('Jim', 'Brown', 18);
-- INSERT INTO employees (First_name, Last_name, Age) VALUES ('Janet', 'Rose', 17);

-- .read sql_syntax_basics.sql

-- SELECT First_name FROM employees;
-- SELECT First_name, Age FROM employees;

-- SELECT First_name FROM employees WHERE First_name IS 'Jack';
-- SELECT First_name FROM employees WHERE Age = 19;
-- SELECT First_name FROM employees WHERE Age > 18;
-- SELECT Last_name, Age FROM employees WHERE Last_name IS NOT 'Black';
-- SELECT Last_name FROM employees WHERE Last_name IS NOT 'Black' AND Age >18;

-- SELECT * FROM employees WHERE First_name LIKE 'Ja%';
-- SELECT * FROM employees WHERE First_name LIKE '%ck' OR Last_name LIKE '%ck';


-- UPDATE

-- UPDATE employees SET First_name = 'Jimm' WHERE First_name = 'Jim';
-- DELETE FROM employees WHERE AGE IS 19;