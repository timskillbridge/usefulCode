

<!-- Constraints are rules which restrict data values-->

<!-- Run sql file in psql \i ./path.sql 
     Run it outside using psql DATABASE_NAME < path.sql
-->

DROP TABLE IF EXISTS student;

CREATE TABLE students(
    id BIGINT NOT NULL
);

<!-- Don't forget the ; after the table creation! -->

<!-- Can modify table data values after creating it using INSERT INTO -->

INSERT INTO student (id) VALUES (0);

<!-- can make the table better by foring ids to be unique -->

CREATE TABLE students(
    id BIGINT NOT NULL UNIQUE
);

<!-- ^ UNIQUE forces unique id values -->

DROP TABLE IF EXISTS employee;

CREATE TABLE employee(
    id BIGINT PRIMARY KEY
);

<!-- ^ PRIMARY KEY forces NOT NULL and UNIQUE -->

<!-- force auto generated primary key -->

DROP TABLE IF EXISTS user (
    id BIGINT GENERATED BY DEFAULT AS IDENTY PRIMARY KEY
);

<!-- add some other fields to the user table -->

DROP TABLE IF EXISTS my_user (  <!-- user is a reserved keyword, use a variation-->
    id BIGINT GENERATED BY DEFAULT AS IDENTY PRIMARY KEY,
    email VARCHAR NOT NULL UNIQUE,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL
);

<!-- insert my_user into the above user table -->

INSERT INTO my_user (email, first_name, last_name) <!-- don't put a semicolon here, the next line is part of the command -->
VALUES ('bob@gmail.com, 'bob', 'render');

<!-- add constraint to a movie in a table created below using REGEX-->
      
<!-- 
accept A-z 0-9 _ - : ' SPACE : '^[A-Za-z0-9 _\-:''\\]+$'
require Title Case : key_name = INITCAP(key_name)
require Title case and A-z0-9 SPACE and -: key_name ~ '^[A-Z][A-Za-z0-9 -]*( [A-Z][A-Za-z0-9 -]*)*$'

 -->

DROP TABLE IF EXISTS movie;

CREATE TABLE movie (
    id BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    name VARCHAR UNIQUE CHECK (name ~ '^[A-Z][a-z]*$'),
    age_limit INT CHECK (age_limit BETWEEN 0 AND 18)
);

<!--  age limit could also be
age_limit INT CHECK (age_limit >0 AND age_limit <= 18)
 -->

 <!-- apply in store.sql -->


 <!-- Relationships 
 Foreign Key ( constraint kind of)
one-to-one
one-to-many
many-to-many 
 -->

<!-- FOREIGN KEY -->

DROP TABLE IF EXISTS passenger;
CREATE TABLE passenger (
    id BIGINT GENERATED BY DEFAULT AS IDENTY PRIMARY KEY,
    name VARCHAR NOT NULL
);

DROP TABLE IF EXISTS passport;
CREATE TABLE passport (
    id BIGINT GENERATED BY AS IDENTITY PRIMARY KEY,
    passport_number VARCHAR UNIQUE NOT NULL,
    passenger_id BIGINT NOT NULL,           <!-- column needs to exist -->
    FOREIGN KEY (passenger_id) REFERENCES passenger(id)  <!--then it can have the foreign key constraing added -->
)

INSERT INTO passenger (name) VALUES ('alice');
INSERT INTO passport (passport_number) VALUES ('XYZ123');
<!-- can insert into multiple on same line -->
INSERT INTO passport(passport_number,passenger_id) VALUES ('ABC123, 12);

<!-- 
    Key Relationships with FOREIGN KEYs
----------------------------------------------

    One-to-one

    Referencing a releationship with two uniuq keys results in a 1:1 relationship

    One-to-many

    Reference one unique key results in one-to-many

    many-to-many

    Requires a side table

    DROP TABLE IF EXISTS student CASCADE;
    CREATE TABLE university (
        id BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
        name VARCHAR NOT NULL
    );

    CREATE TABLE student (
        id BIGINT CREATED BY DEFAULT AS IDENITTY PRIMARY KEY,
        name VARCHAR NOT NULL,
        university_id as BIGINT,  <---- the FOREIGN KEY
            FOREIGN KEY (university_id) REFERENCES university(id)
    );

    INSERT INTO students (name, university_id) VALUES ('Alice', 1);
    INSERT INTO students (name, university_id) VALUES ('Bob', 1);

    CREATE TABLE course (
        id BIGINT CREATED BY DEFAULT AS IDENTITY PRIMARY KEY,
        name VARCHAR NOT NULL UNIQUE
    );

    INSERT INTO COURSE (name) VALUES ('math');
    INSERT INTO COURSE (name) VALUES ('english')

<!-- create joined table
        CREATE TABLE student_course (
        id BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
        student_id,
        FOREIGN KEY (student_id) REFERENCES student(id);
        course_id,
        FOREIGN KEY (course_id) REFERENCES course(id),
        CONSTRAINT UNIUQE (student_id, course_id)
    )

INSERT INTO student_course (student_id, course_id) VALUES (1,1);
INSERT INTO student_course (student_id, course_id) VALUES (1,2);
INSERT INTO student_course (student_id, course_id) VALUES (2,1);
INSERT INTO student_course (student_id, course_id) VALUES (2,2);

----------------------------------------------
    Active and non-active table items

    use a boolean true false value to determine if a table (like a user) is active or inactive

    Ex:
    DROP TABLE IF EXISTS user CASCADE;
    CREATE TABLE user (
    id BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    name VARCHAR NOT NULL
    is_active BOOLEAN)
    
-->


