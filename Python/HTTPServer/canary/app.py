import os

from canary import create_app  # noqa

def_env = 'development'
env = os.getenv('FLASK_CONFIG', def_env)
app = create_app(env)

