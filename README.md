# django-crud

A CRUD API using Django Rest Framework

## Get Started
1. Clone the repository: https://github.com/Kanza12345/django-crud.git
2. Run: ```python manage.py runserver```

## How to

Read: ```curl --request GET http://127.0.0.1:8000/api/counsellors```
Create: ```curl --request POST  http://127.0.0.1:8000/api/counsellors --header "Content-Type: application/json" --data '{body}'```
Update: ```curl --request PUT  http://127.0.0.1:8000/api/counsellors/{uuid} --header "Content-Type: application/json" --data '{body}'```
Delete: ```curl --request DELETE http://127.0.0.1:8000/api/counsellors/{uuid}```

This Example shows accessing the API for the counsellor model. The same can be applied for the Patient and Appointment Model.