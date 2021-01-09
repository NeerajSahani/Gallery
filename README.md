# Gallery

### Steps to use

##### 1 Create & Load Virtual Environment
```bash
$ python -m venv .env
$ "./env/Scripts/activate"
```

##### 2 Install required libraries
```bash
$ pip install -r requirements.txt
```

##### 3 Setup Database
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

##### 4 Run Server
```bash
$ python manage.py runserver
```


### Features
<ul>
    <li>Tag Form</li>
    <li> Image Form </li>
    <li> Basic Image Gallery </li>
    <li> Filter Images by Tags by clicking on tags </li>
    <li> Rotate Images </li>
    <li> Popup Tag Form </li>
</ul>