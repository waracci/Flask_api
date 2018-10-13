from app.apps import create_app
import os

app = create_app(os.getenv('APP_SETTINGS'))


if __name__=='__main__':
    app.run()
