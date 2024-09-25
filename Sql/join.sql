
create database company

select * from employe

select * from dprt

insert into employe(emp_id , name) VALUES(1,'Rex') , (2,'Sam') , (3,'Ram')

insert into dprt(dprt_id , dprt) VALUES (2,'Web') , (3,'Android')

CREATE VIEW employe_dprt AS 
SELECT employe.emp_id, employe.name, dprt.dprt 
FROM employe 
FULL JOIN dprt ON employe.emp_id = dprt.dprt_id;


select * from employe_dprt


