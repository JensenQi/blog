# -*- coding: utf-8 -*-
from flask.ext.script import Manager, Server
from config import HOST, PORT

from api import create_app

app = create_app()
manager = Manager(app)
server = Server(host=HOST, port=PORT, use_debugger=True)
manager.add_command('runserver', server)


@manager.command
def build_db():
    import models
    models.build_db()


if __name__ == '__main__':
    manager.run()
