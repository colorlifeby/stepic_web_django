# nginx
sudo ln -sf /home/box/web/etc/box.conf  /etc/nginx/conf.d
sudo /etc/init.d/nginx restart

# gunicorn
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/wsgi.py /etc/gunicorn.d/wsgi.py 
sudo /etc/init.d/gunicorn restart

# mysql
sudo /etc/init.d/mysql restart
sudo mysql -uroot -e "DROP DATABASE IF EXISTS ask"
sudo mysql -uroot -e "CREATE DATABASE ask"
sudo mysql -uroot -e "CREATE USER 'askuser'@'localhost' IDENTIFIED BY '11111'"
sudo mysql -uroot -e "GRANT ALL PRIVILEGES ON ASK.* TO 'askuser'@'localhost' IDENTIFIED BY '11111'" 