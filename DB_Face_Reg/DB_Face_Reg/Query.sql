use student;


create table stu_details
(
	Reg_no varchar(100),
    stu_name varchar(100),
    dept varchar(100),
    dob varchar(100),
    stu_year varchar(100),
    start_year varchar(100),
    phone_no varchar(100),
    address varchar(200),
    attend varchar(100),
    dt datetime
);

create table results
(
	Reg_no varchar(100),
    cgpa varchar(100)
);

create table course
(
	c_id varchar(100),
    c_name varchar(100),
    handle varchar(100),
    credits varchar(100)
);

create table Student
(
	Reg_no varchar(100),
    c_id varchar(100)
);


select * from course;
select * from Student;
select * from results;
select * from stu_details;

drop table course,Student,results,stu_details;