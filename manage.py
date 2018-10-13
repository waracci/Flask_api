import os
import unittest
import logging
from flask_script import Manager

from app.apps import create_app

logging.basicConfig()
app = create_app(config_name=os.getenv('APP_SETTINGS'))

manager = Manager(app)

@manager.command
def run_tests():
    """Runs the unitests without test coverage"""
    app_tests = unittest.TestLoader().discover('./app/tests/v1', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(app_tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__=='__main__':
    manager.run()