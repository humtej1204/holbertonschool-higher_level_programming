-- Script that creates a table second_table in the database hbtn_0c_0 and add multiples rows
CREATE TABLE IF NOT EXISTS second_table(id INT, name VARCHAR(256), score INT);
INSERT INTO second_table value('1', 'John', '10');
INSERT INTO second_table value('2', 'Alex', '3');
INSERT INTO second_table value('3', 'Bob', '14');
INSERT INTO second_table value('4', 'George', '8');
