

DROP TABLE IF EXISTS students;

CREATE TABLE students (
    -- id INT PRIMARY KEY,
    id SERIAL PRIMARY KEY,
    -- VARCHAR(50) limits input to 50 characters and only stores what is actually used
    -- CHAR(50) does the same but always reserves 50 characters
    first_name VARCHAR(50),
    age INT,
    -- grade can be up to 2 characters with the + or -
    grade VARCHAR(2)
    );

-- do not use double quotes or caps for naming database or tables
\COPY students FROM 'path to csv file' DELIMITER ',' CSV HEADER;

-- * will SELECT all fields
SELECT * FROM students;

-- You can specify them by name
SELECT first_name, last_name
FROM students;

-- can count them, group them by field name
SELECT COUNT(*) from students
GROUP BY grade;

-- inserting data is a query and requires a semicolon ;
INSERT INTO students (id, first_name, last_name, age, grade) VALUES
('Tim', 'Adams', 42, 'B-');

SELECT COUNT(*) FROM students;

SELECT * FROM students;

INSERT INTO students (first_name,last_name,age,grade) VALUES
('Bill','Jenkins',35,'C');

-- drop a record
DELETE DATA FROM students WHERE first_name = 'Tim';

SELECT * From students;