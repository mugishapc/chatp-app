# This must be the VERY FIRST import/statement
import eventlet
eventlet.monkey_patch()

# Now import other modules
from app import app, db
from flask_migrate import Migrate
from flask.cli import FlaskGroup

# Initialize migrate
migrate = Migrate(app, db)

# Use Flask CLI
cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    """Create the database tables"""
    with app.app_context():
        db.create_all()
    print("Database tables created!")

if __name__ == "__main__":
    cli()