

Database schema design refers to the process of definig the strucute that
represents the organization fo data in a databalse.

Good practice

1. Don't duplicate data; make it accessible from one place
2. one piece of data per field
3. each column represents a single type of data
4. use primary keys
5. name foreign keys as the table to whcih they point with _id appended
    table user is referenced in table activity with the foreign key user_id within table activity
6. be consistent with names
    lowercase
    use underscores to separate words or abbreviations
    use singular or plural, not both
    be specific with names, not vague


PostgreSQL and PSQL Command CheatSheet
PSQL
Connect to a Database

psql -d <database>
What it's used for?
Connects to the specified PostgreSQL database.
Default value and when to change this value
Default is the user's default database. Change when connecting to a specific database.
Specify Host

psql -h <host>
What it's used for?
Specifies the host server to connect to.
Default value and when to change this value
Default is local host. Change when connecting to a remote server.
Specify Port

psql -p <port>
What it's used for?
Specifies the port number to connect to.
Default value and when to change this value
Default is 5432. Change when PostgreSQL is running on a different port.
Specify Username

psql -U <username>
What it's used for?
Specifies the username to connect with.
Default value and when to change this value
Default is the operating system's current user. Change when connecting with a different user.
Run SQL File (Local Machine)

psql -d <database> -U <username> -f <path/to/sqlfile.sql>
What it's used for?
Executes SQL commands from a file on the local machine.
How to use it
Replace <database> with the desired database name, <username> with the PostgreSQL username, and <path/to/sqlfile.sql> with the path to the SQL file.
When to use it
When you want to run SQL commands stored in a file.
Short Hand
psql <database> < <path/to/sqlfile.sql>
PostgreSQL
Create Database

<!-- bash shortcut command -->
createdb <database>
<!-- within postgresql -->
CREATE DATABASE <database>;
What it's used for?
Creates a new PostgreSQL database.
How to use it
Replace <database> with the desired database name.
When to use it
When you need to create a new database.
Connect to a Database

\c <database>
What it's used for?
Connects to the specified PostgreSQL database within the psql shell.
How to use it
Replace <database> with the desired database name.
When to use it
When you want to switch to a different database within the psql shell.
List Databases

\l
What it's used for?
Lists all available databases.
How to use it
Enter the command within the psql shell.
When to use it
When you need to view the existing databases.
List Tables

\dt
What it's used for?
Lists all tables in the current database.
How to use it
Enter the command within the psql shell.
When to use it
When you want to view the tables in the current database.
Run SQL File (Current Database)

\i <path/to/sqlfile.sql>
What it's used for?
Executes SQL commands from a file within the psql shell.
How to use it
Replace <path/to/sqlfile.sql> with the path to the SQL file.
When to use it
When you want to run SQL commands stored in a file within the psql shell.
Quit psql

\q
What it's used for?
Exits the psql shell.
How to use it
Enter the command within the psql shell.
When to use it
When you want to exit the psql shell and return to the command line.
