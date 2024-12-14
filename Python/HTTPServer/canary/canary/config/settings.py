import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class BaseConfig:
    DEFAULT_SECRET_KEY = 'wwzgYXYPI/ytEfA4wP1W5KucP21vaDaiusGaO5OlaOBw5O1Bg1f3nmg+G0VkauQPQEodiI4AKXF05rLPNmvquFYC'
    SECRET_KEY = os.getenv('SECRET_KEY', DEFAULT_SECRET_KEY)


# 开发环境
class DevelopmentConfig(BaseConfig):
    DEBUG = True


# 测试环境
class TestingConfig(BaseConfig):
    DEBUG = False


# 生产环境
class ProductionConfig(BaseConfig):
    DEBUG = False

    # 默认数据源
    SQLALCHEMY_DATABASE_URI = 'mysql://ro_guest:9527#RDS@rm-bp18623422m8o2n7x1o.mysql.rds.aliyuncs.com/db1'
    # 多数据源
    SQLALCHEMY_BINDS = {
        'db1': 'mysql://ro_guest:9527#RDS@rm-bp18623422m8o2n7x1o.mysql.rds.aliyuncs.com/db1',
        'db2': 'mysql://ro_guest:9527#RDS@rm-bp18623422m8o2n7x1o.mysql.rds.aliyuncs.com/db2'
    }


environment_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
