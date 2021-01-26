

news_key = 'ab66c4c574b34921bebbf9f8503859aa'


class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:1234@localhost/test1'
    SECRET_KEY = 'MADI04'
    SECURITY_PASSWORD_SALT = 'not None'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'