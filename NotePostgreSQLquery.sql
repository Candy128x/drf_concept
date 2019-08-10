DESCRIBE empapi_empinfo;
SHOW CREATE TABLE empapi_empinfo;
SHOW TABLES LIKE '%key_word%';
SHOW INDEX FROM table_name;
SELECT * FROM table_name;

pg_dump -t empapi_empinfo -s;

select column_name, data_type, character_maximum_length
from INFORMATION_SCHEMA.COLUMNS where table_name = 'empapi_empinfo';

SELECT *
FROM info_schema.columns
WHERE table_schema = 'empapi_empinfo';

---
SELECT * FROM table_name ORDER BY 1 DESC;
SELECT * FROM languages_language ORDER BY 1 DESC;
SELECT * FROM languages_paradigm ORDER BY 1 DESC;
SELECT * FROM languages_programmer ORDER BY 1 DESC;
SELECT * FROM languages_programmer_languages ORDER BY 1 DESC;
SELECT * FROM empapi_empinfo ORDER BY 1 DESC;
SELECT * FROM empapi_companylist ORDER BY 1 DESC;

-- inner join
SELECT * FROM languages_programmer as lp
INNER JOIN languages_programmer_languages AS lpl ON (lp.id = lpl.programmer_id)
INNER JOIN languages_language AS ll ON (lpl.language_id = ll.id)
ORDER BY lp.id DESC;


--
select * from empapi_companylist


---
insert into 
empapi_companylist(name, salary, date_of_join, experience, emp_id)
values ('TCS', 18000, '2018-02-01', 3, 2);


---
delete from empapi_companylist 
where id in (5,6,7,8);


---
drop table empapi_companylist;

--inner join
select cl.emp_id, * from empapi_companylist as cl
inner join empapi_empinfo as ei on (cl.emp_id = ei.id)
where cl.experience >= 2
group by cl.emp_id
order by ei.id desc;



-- group by
select distinct on (emp_id) 'def', *.*
from empapi_companylist as cl
inner join empapi_empinfo as ei (cl.emp_id = ei.id)
order by emp_id desc;









