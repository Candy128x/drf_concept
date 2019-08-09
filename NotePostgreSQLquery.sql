DESCRIBE table_name;
SHOW CREATE TABLE table_name;
SHOW TABLES LIKE '%key_word%';
SHOW INDEX FROM table_name;
SELECT * FROM table_name;


---
SELECT * FROM table_name ORDER BY 1 DESC;
SELECT * FROM languages_language ORDER BY 1 DESC;
SELECT * FROM languages_paradigm ORDER BY 1 DESC;
SELECT * FROM languages_programmer ORDER BY 1 DESC;
SELECT * FROM languages_programmer_languages ORDER BY 1 DESC;


-- inner join
SELECT * FROM languages_programmer as lp
INNER JOIN languages_programmer_languages AS lpl ON (lp.id = lpl.programmer_id)
INNER JOIN languages_language AS ll ON (lpl.language_id = ll.id)
ORDER BY lp.id DESC;


