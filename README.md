# student-record-mgmt

# Cretaing virtual env and installing packages
    $ virtualenv env
    
    $ source env/bin/activate(linux)

    $ .\env\Script\activate(windows)

    $ pip install -r requirements.txt
    
# Setting up database
    -Go to /student_mgmt/student_mgmt/settings.py and make changes in data base confoguration shown as below
    <pre>
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'student_db',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': 'localhost'
        }
    }
    </pre>
    
# Running application
    $ cd student_mgmt
    $ python manage.py runserver
