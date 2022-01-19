from flask import Flask
import routes.routes as routes
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {"pool_pre_ping": True}  
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://root:root@localhost:5439/root"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Endpoints
app.add_url_rule('/', view_func=routes.home, methods=['GET'])
app.add_url_rule('/all', view_func=routes.handle_all, methods=['GET'])
app.add_url_rule('/find/<int:id_item>', view_func=routes.handle_find_one, methods=['GET'])
app.add_url_rule('/save', view_func=routes.handle_save, methods=['POST'])

if __name__ == '__main__':
        app.run(host='127.0.0.1',  debug=True)