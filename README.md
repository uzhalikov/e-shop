1. python -m venv venv              #create venv
2. source venv/bin/activate         #activate venv
3. pip3 install -r requirements.txt #install dependencies
4. python manage.py makemigrations  #create migrations
5. python manage.py migrate         #confirm migrations
6. python manage.py runserver       #run server
7. go to the link localhost:8000    #visit site