from werkzeug.middleware.profiler import ProfilerMiddleware
from flask_sqlalchemy import SQLAlchemy

from backend import create_app

db = SQLAlchemy()

app = create_app()
db.init_app(app)

if __name__ == "__main__":
    app.run(debug = True)
