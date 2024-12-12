import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class BaseConfig:
    DEFAULT_SECRET_KEY = 'wwzgYXYPI/ytEfA4wP1W5KucP21vaDaiusGaO5OlaOBw5O1Bg1f3nmg+G0VkauQPQEodiI4AKXF05rLPNmvquFYC'
    SECRET_KEY = os.getenv('SECRET_KEY', DEFAULT_SECRET_KEY)


# 开发环境
class DevelopmentConfig(BaseConfig):
    DEBUG = True
    # 默认数据源
    SQLALCHEMY_DATABASE_URI = 'mysql://<用户名>:<密码>@rm-xxx.mysql.rds.aliyuncs.com:3306/db0'
    # 多数据源
    SQLALCHEMY_BINDS = {
        'db1': 'mysql://<用户名>:<密码>@rm-xxx.mysql.rds.aliyuncs.com:3306:3306/db1',
        'db2': 'mysql://<用户名>:<密码>@rm-xxx.mysql.rds.aliyuncs.com:3306:3306/db2'
    }


# 测试环境
class TestingConfig(BaseConfig):
    DEBUG = False


# 生产环境
class ProductionConfig(BaseConfig):
    DEBUG = False


environment_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
