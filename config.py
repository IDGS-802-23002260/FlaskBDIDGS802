class Config(object):
    SECRET_KEYA="Clave nueva"
    SESSIONS_COOKIE_SECURE=False

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:quegay @localhost:3306/dbidgs802"
    SQLALCHEMY_TRACK_MODIFICATION=False