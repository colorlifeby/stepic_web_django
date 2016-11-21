# nginx
sudo ln -sf /home/box/web/etc/box.conf  /etc/nginx/conf.d
sudo /etc/init.d/nginx restart

# gunicorn
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/wsgi.py /etc/gunicorn.d/wsgi.py 
sudo /etc/init.d/gunicorn restart
