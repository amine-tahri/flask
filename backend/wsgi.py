from werkzeug.middleware.profiler import ProfilerMiddleware
from flask_sqlalchemy import SQLAlchemy

from backend import create_app
db = SQLAlchemy()

app = create_app()
db.init_app(app)
if __name__ == "__main__":
    app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions = [10])
    app.run(debug = True)
