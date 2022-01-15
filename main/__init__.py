from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_admin import Admin
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '2008de4bbf105d61f26a763f8ee8023b'
# # database = 'postgres://dimacs:@Dimacs254db@dimacsinternational.com:5432/dimacs_db'
# database = 'postgres://efyuozoupivpft:1554341dc42200a4cc6c0c62a945e9be776ae462cfb5ee66555cbdd984ebda3b@ec2-54-78-36-245.eu-west-1.compute.amazonaws.com:5432/d85737oc3ecsc7'
# app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {"pool_pre_ping": True}
# app.config['SQLALCHEMY_DATABASE_URI'] = database
# db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
# admin = Admin(app, name='Dimacs')
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'
# login_manager.login_message_category = 'info'
#
#
# app.config['MAIL_SERVER'] = 'mail.dimacsinternational.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'clients@dimacsinternational.com'
# app.config['MAIL_PASSWORD'] = '@D_client2120'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
# mail = Mail(app)


from main import routes
