Для степика:
- в ask/settings.py
  1. ALLOWED_HOSTS = [] 
  2. TEMPLATE_DIRS = (
       BASE_DIR + '/templates',
     ) 
- в init.sh 
  1. поменять миграцию.
  2. Первый раз разкоментить создание юзера
