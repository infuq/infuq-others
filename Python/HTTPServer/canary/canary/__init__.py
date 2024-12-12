import pkgutil
import sys

import pymysql
from flask import Flask, Blueprint

from canary.config.settings import environment_config
from canary.core.extensions import db


def create_app(env):
    app = Flask('canary')
    config = environment_config[env]
    app.config.from_object(config)
    # 解决中文乱码问题
    app.json.ensure_ascii = False

    # views
    auto_register_blueprint(app)

    # extensions
    pymysql.install_as_MySQLdb()
    db.init_app(app)

    return app

# 自动注册蓝图
def auto_register_blueprint(app: Flask):
  app_dict = {}
  pkg_list = pkgutil.walk_packages(__path__, __name__ + ".")
  for _, module_name, ispkg in pkg_list:
    __import__(module_name)
    module = sys.modules[module_name]
    module_attrs = dir(module)
    for name in module_attrs:
      var_obj = getattr(module, name)
      if isinstance(var_obj, Blueprint):
        if app_dict.get(name) is None:
          app_dict[name] = var_obj
          app.register_blueprint(var_obj)
          print("> 注入%s模块%s\t成功" % (Blueprint.__name__, var_obj.__str__()))
