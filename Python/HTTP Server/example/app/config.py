class BaseConfig(object):
    DEBUG = True
    YEAR = 2024
    ADDRESS = 'beijing'
    DATE = '2024-11-15'

class ProdConfig(BaseConfig):
    DB_URL = 'mysql...'

