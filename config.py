WTF_CSRF_ENABLED = True
SECRET_KET = 'Kbq39wse'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db/landscaping.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db/db_repository')