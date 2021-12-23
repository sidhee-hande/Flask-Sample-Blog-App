DEBUG= True
USERNAME= 'sidhee'
PASSWORD= '123'
SECRET_KEY='you will never guess this'
SQLALCHEMY_DATABASE_URI = 'sqlite:///flask_blog.db'
SQLALCHEMY_TRACK_MODIFICATIONS= True

import os
basedir = os.path.abspath(os.path.dirname(__file__))

    # ...
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False