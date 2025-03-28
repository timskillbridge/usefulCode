

DROP TABLE IF EXISTS game;
CREATE TABLE game (
    --don't forget to match order and spelling any csv headers you're importing
    game_id BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    game_title VARCHAR(100) UNIQUE NOT NULL  --no comma, next line is part of this line
        CHECK(game_title ~ '^[A-Za-z0-9 _/-:''\\]+$/g'), --starts with letter, num, or special char
    quantity INT NOT NULL
        CHECK(quantity BETWEEN 0 AND 100) DEFAULT 0, -- default alue 
    price DECIMAL(5,2) NOT NULL
        CHECK(price BETWEEN 10 AND 60) DEFAULT 0,  -- BETWEEN is inclusive
    discount_price DECIMAL
        CHECK(discount_price > price)

)

INSERT INTO game (game_title)
VALUES ('My game');

-- end of Constraints

-- Relationships

-- 1. FOREIGN KEY
DROP TABLE IF EXISTS employee;
CREATE TABLE employee(
    id BIGINT GENERATED BY DEFAULT AS IDENTY PRIMARY KEY,
    name VARCHAR NOT NULL
);

-- import data for employees
\COPY employee FROM 'path/to/data/epmloyee.csv' WITH CSV HEADER;
SELECT setval('epmloyee_id_seq', (SELECT MAX(id) FROM epmloyee));

DROP TABLE IF EXISTS employee_hr_record
CREATE TABLE employee_hr_record (
    id BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    employee_ssn VARCHAR(11) UNIQUE,
    employee_id BIGINT NOT NULL,
    FOREIGN KEY (epmloyee_id) REFERENCES epmloyee (id)
);

INSERT INTO employee (name) VALUES ('alice');
INSERT INTO employee (name) VALUES ('bob');

-- CASCADE deletes everything relying on the thing you're trying to delete

DROP TABLE IF EXISTS passenger CASCADE; --
CREATE TABLE passenger (
    id BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    name VARCHAR NOT NULL
);

DROP TABLE IF EXISTS passport;
CREATE TABLE PASSPORT (
    id BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    passport_number VARCHAR UNIQUE NOT NULL,
    passenger_id BIGING NOT NULL,
    FOREIGN KEY (passenger_id) REFERENCES passenger (id) on DELETE CASCADE -- will allow you to delete 
                                                                           -- passenger this will also delete
)


-- employees many to many

DROP TABLE IF EXISTS employee CASCADE;

CREATE TABLE store (
    id BIGINT GENERATED BY DEFAULT AS PRIMARY KEY,
    name VARCHAR NOT NULL
);

CREATE TABLE epmloyee (
    int BIGINT GENERATED BY DEFAULT AS PRIMARY KEY,
    name VARCHAR NOT NULL,
    store_id as BIGINT,
    FOREIGN KEY (store_id) REFERENCES store (id)
);

INSERT INTO epmloyee (name, store_id) VALUES ('Alice',1);
INSERT INTO epmloyee (name, store_id) VALUES ('Bob',2);

CREATE TABLE training_course (
    id BIGINT GENERATED BY DEFAULT AS PRIMARY KEY,
    name VARCHAR NOT NULL UNIQUE
);

INSERT INTO training_course (name) VALUES ('using_the_register');
INSERT INTO training_course (name) VALUES ('loading_dock_safety');

-- create joined-table to connect the employee and store tables

CREATE TABLE epmloyee_training (
    PRIMARY KEY (epmloyee_id, training_course_id), -- prevents duplicates in many-to-many relationship
    epmloyee_id BIGINT,
    FOREIGN KEY (epmloyee_id) REFERENCES epmloyee (id),
    training_id BIGING,
    FOREIGN KEY (training_course_id) REFERENCES training_course (id)
)

--  can accomplish preventing duplicate many-to-many.  Better way to do it.
CREATE TABLE epmloyee_training (
    id BIGINT GENERATED BY DEFAULT AS PRIMARY KEY,
    epmloyee_id BIGINT,
    training_course_id BIGINT,
    CONSTRAINT UNIQUE (epmloyee_id, training_course_id),
    FOREIGN KEY (epmloyee_id) REFERENCES epmloyee (id),
    FOREIGN KEY (training_course_id) REFERENCES training_course (id)
)
