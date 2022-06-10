from flask import Flask, session, request, g, render_template
import pymysql
from exts import db
from flask_migrate import Migrate
from blueprints import administration_bp, affair_bp, home_bp, jiaowu_bp, login_bp, project_bp, resource_bp, system_bp
from models import UserModel
import config

pymysql.install_as_MySQLdb()

app = Flask(__name__, template_folder='templates', static_url_path='/', static_folder='')
app.config.from_object(config)
db.init_app(app)
migrate = Migrate(app, db)
app.register_blueprint(administration_bp)
app.register_blueprint(affair_bp)
app.register_blueprint(home_bp)
app.register_blueprint(jiaowu_bp)
app.register_blueprint(login_bp)
app.register_blueprint(project_bp)
app.register_blueprint(resource_bp)
app.register_blueprint(system_bp)


@app.before_request
def before_request():
    user_id = session.get('userid')
    if user_id:
        try:
            user = UserModel.query.get(user_id)
            if user:
                g.user = user
        except Exception as e:
            print(e)
            g.user = ''

    url = request.path
    lis01 = ['/login', '/register']
    if url in lis01 or url.endswith('.ico') or url.endswith('.png') or url.endswith('.bmp') or url.endswith('.css'):
        pass
    elif not session.get('userid'):
        return render_template('login/login.html')


@app.context_processor
def context_processor():
    if hasattr(g, 'user'):
        return {'user': g.user}
    return {}


if __name__ == '__main__':
    app.run()
