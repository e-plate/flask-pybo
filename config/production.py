from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'R\\\xe8\xed\xae\xe6!/}\xda \xc5\xdc\xcc\xb2z'
#-------#