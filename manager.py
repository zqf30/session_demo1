from flask_script import Manager
from app import app
from flask_migrate import Migrate, MigrateCommand
from exts import db

manager = Manager(app)
# 1. before user 'flask_migrate', give params 'app' and 'db'
migrate = Migrate(app, db)
# 2. add 'migrateCommand' to manager
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()