SECRET_KEY = 'django-insecure-kp@gkt*nb53((t_f%j)' \
             'hjfq_wnbg=b@e=4&bo0^jy-eopbv$^*'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'my_day',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
                    }
    }
}
