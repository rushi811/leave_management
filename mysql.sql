use training;
create table leave_table(id int primary key,
description varchar(255),
start_date DATE,
end_date DATE,
status varchar(30)
);
insert into leave_table(id, description, start_date, end_date,status)
values (100,"paid-leave","2023-02-18", "2023-02-28","pending");
SELECT CONCAT(id ,"  ",status) AS "Status of leave" FROM leave_table;
SELECT status from leave_table; 
