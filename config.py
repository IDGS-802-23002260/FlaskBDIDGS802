class Config(object):
    SECRET_KEY = "Clave nueva"  # <- nombre correcto
    SESSION_COOKIE_SECURE = False  # <- typo corregido

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://flaskuser:1234@127.0.0.1:3306/bdidgs802"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # <- typo corregido