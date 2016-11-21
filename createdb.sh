# mysql
sudo /etc/init.d/mysql restart
mysql -uroot -e "DROP DATABASE IF EXISTS ask"
mysql -uroot -e "CREATE DATABASE ask"
# mysql -uroot -e "CREATE USER 'askuser'@'localhost' IDENTIFIED BY '11111'"
mysql -uroot -e "GRANT ALL PRIVILEGES ON ask.* TO 'askuser'@'localhost';"

#sudo python /home/box/web/ask/manage.py syncdb
sudo python /home/box/web/ask/manage.py makemigrations qa
sudo python /home/box/web/ask/manage.py migrate

mysql -uroot -e "USE ask; INSERT INTO ask.auth_user(id,username) VALUES (1,'Author 1')"
mysql -uroot -e "USE ask; INSERT INTO ask.auth_user(id,username) VALUES (2,'Author 2')"
mysql -uroot -e "USE ask; INSERT INTO ask.auth_user(id,username) VALUES (3,'Author 3')"



mysql -uroot -e "USE ask; INSERT INTO ask.qa_question(title,text,rating, author_id) VALUES ('Question title 01','question text 1',6,1)"
mysql -uroot -e "USE ask; INSERT INTO ask.qa_question(title,text,rating, author_id) VALUES ('Question title 02','question text 2',1,2)"
mysql -uroot -e "USE ask; INSERT INTO ask.qa_question(title,text,rating, author_id) VALUES ('Question title 03','question text 3',6,3)"
mysql -uroot -e "USE ask; INSERT INTO ask.qa_question(title,text,rating, author_id) VALUES ('Question title 04','question text 4',6,1)"
mysql -uroot -e "USE ask; INSERT INTO ask.qa_question(title,text,rating, author_id) VALUES ('Question title 05','question text 5',22,1)"
mysql -uroot -e "USE ask; INSERT INTO ask.qa_question(title,text,rating, author_id) VALUES ('Question title 06','question text 6',5,1)"
mysql -uroot -e "USE ask; INSERT INTO ask.qa_question(title,text,rating, author_id) VALUES ('Question title 07','question text 7',12,3)"
mysql -uroot -e "USE ask; INSERT INTO ask.qa_question(title,text,rating, author_id) VALUES ('Question title 08','question text 8',3,2)"
mysql -uroot -e "USE ask; INSERT INTO ask.qa_question(title,text,rating, author_id) VALUES ('Question title 09','question text 9',0,2)"
mysql -uroot -e "USE ask; INSERT INTO ask.qa_question(title,text,rating, author_id) VALUES ('Question title 10','question text 10',3,1)"
mysql -uroot -e "USE ask; INSERT INTO ask.qa_question(title,text,rating, author_id) VALUES ('Question title 11','question text 11',1,1)"
mysql -uroot -e "USE ask; INSERT INTO ask.qa_question(title,text,rating, author_id) VALUES ('Question title 12','question text 12',2,3)"
mysql -uroot -e "USE ask; INSERT INTO ask.qa_question(title,text,rating, author_id) VALUES ('Question title 13','question text 13',4,3)"
mysql -uroot -e "USE ask; INSERT INTO ask.qa_question(title,text,rating, author_id) VALUES ('Question title 14','question text 14',1,2)"
mysql -uroot -e "USE ask; INSERT INTO ask.qa_question(title,text,rating, author_id) VALUES ('Question title 15','question text 15',44,2)"
mysql -uroot -e "USE ask; INSERT INTO ask.qa_question(title,text,rating, author_id) VALUES ('Question title 16','question text 16',3,2)"
mysql -uroot -e "USE ask; INSERT INTO ask.qa_question(title,text,rating, author_id) VALUES ('Question title 17','question text 17',2,3)"
mysql -uroot -e "USE ask; INSERT INTO ask.qa_question(title,text,rating, author_id) VALUES ('Question title 18','question text 18',5,1)"
mysql -uroot -e "USE ask; INSERT INTO ask.qa_question(title,text,rating, author_id) VALUES ('Question title 19','question text 19',3,3)"
mysql -uroot -e "USE ask; INSERT INTO ask.qa_question(title,text,rating, author_id) VALUES ('Question title 20','question text 20',2,1)"
mysql -uroot -e "USE ask; INSERT INTO ask.qa_question(title,text,rating, author_id) VALUES ('Question title 21','question text 21',2,2)"
mysql -uroot -e "USE ask; INSERT INTO ask.qa_question(title,text,rating, author_id) VALUES ('Question title 22','question text 22',1,3)"
mysql -uroot -e "USE ask; INSERT INTO ask.qa_question(title,text,rating, author_id) VALUES ('Question title 23','question text 23',13,2)"
mysql -uroot -e "USE ask; INSERT INTO ask.qa_question(title,text,rating, author_id) VALUES ('Question title 24','question text 24',6,2)"
mysql -uroot -e "USE ask; INSERT INTO ask.qa_question(title,text,rating, author_id) VALUES ('Question title 25','question text 25',7,1)"
mysql -uroot -e "USE ask; INSERT INTO ask.qa_question(title,text,rating, author_id) VALUES ('Question title 26','question text 26',8,1)"

mysql -uroot -e "USE ask; INSERT INTO ask.qa_answer(text, question_id, author_id) VALUES ('answer1', 1,1)"
mysql -uroot -e "USE ask; INSERT INTO ask.qa_answer(text, question_id, author_id) VALUES ('answer1', 1,2)"
mysql -uroot -e "USE ask; INSERT INTO ask.qa_answer(text, question_id, author_id) VALUES ('answer1', 1,3)"

mysql -uroot -e "USE ask; INSERT INTO ask.qa_answer(text, question_id, author_id) VALUES ('answer22', 22,2)"

mysql -uroot -e "USE ask; INSERT INTO ask.qa_answer(text, question_id, author_id) VALUES ('answer6', 6,1)"
mysql -uroot -e "USE ask; INSERT INTO ask.qa_answer(text, question_id, author_id) VALUES ('answer6', 6,2)"
mysql -uroot -e "USE ask; INSERT INTO ask.qa_answer(text, question_id, author_id) VALUES ('answer6', 6,3)"


