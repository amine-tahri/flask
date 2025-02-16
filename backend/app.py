from flask import Flask

from flask_cors import CORS
from flask_appbuilder import SQLA, AppBuilder

from users.api import UserRestApi
from articles.api import ArticleRestApi

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Configuration settings
app.config['SECRET_KEY'] = 'dev_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/opide_2'

db = SQLA(app)
appbuilder = AppBuilder(app, db.session)

db.create_all()

appbuilder.add_api(UserRestApi)
appbuilder.add_api(ArticleRestApi)

if __name__ == '__main__':
    app.run(debug=True)