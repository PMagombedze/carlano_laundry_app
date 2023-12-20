class Config:
    DEBUG = True
    SECRET_KEY = '1234567890'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
