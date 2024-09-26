
use company


create table student(


id int PRIMARY KEY,

name varchar(20),

email varchar(30) UNIQUE,

age int NOT NULL,

class int DEFAULT 10

)

create table teacher(

id int , 

teacher_name varchar(20) , 

FOREIGN KEY (id) REFERENCES student(id)

)

INSERT INTO student (id,name,email,class) VALUES (1,'Rex','rex@mail.com',20)

ALTER TABLE student
ALTER COLUMN age INT NULL;



SELECT * FROM student

SELECT * FROM teacher