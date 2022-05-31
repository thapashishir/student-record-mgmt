
<h2>Creating Application</h2>
<li>python manage.py startapp registration</li>

<h2>Add your app name in installed apps.</h2>
<p>To add created application on your project you need to modified followin codes in /student_mgmt/settings.py
<pre>
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registration'
]
</pre>
<h2>Configure template folder for application</h2>
<p>To configure the Django template system, go to the settings.py file and update the DIRS to the path of the templates folder. Generally, the templates folder is created and kept in the sample directory where manage.py lives. This templates folder contains all the templates you will create in different Django Apps.</p>
<pre>
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
</pre>
<h2>Configure and register student list url</h2>
<li>Create urls.py file in registration and add following code</li>
<pre>

</pre>



 
