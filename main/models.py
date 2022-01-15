# from datetime import datetime
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# from main import db, login_manager, app, admin
# from flask_login import UserMixin
# from flask import session, abort
# from flask_admin.contrib.sqla import ModelView
# from flask_login import current_user
#
#
# @login_manager.user_loader
# def load_user(user_id):
#     if session['account_type'] == 'Employer':
#         return Employers.query.get(int(user_id))
#     elif session['account_type'] == 'User':
#         return User.query.get(int(user_id))
#     else:
#         return None
#
#
# # Joining (relationship) table for Users and jobs
# # workers = db.Table('workers',
# #                    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
# #                    db.Column('job_id', db.Integer, db.ForeignKey('jobs.job_id'))
# #                    )
# #
#
# class Workers(db.Model):
#
#     __tablename__ = 'workers'
#
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
#     job_id = db.Column(db.Integer, db.ForeignKey('jobs.job_id'))
#
#
# class User(db.Model, UserMixin):
#
#     __tablename__ = 'user'
#
#     def get_id(self):
#         return self.user_id
#
#     user_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), unique=True, nullable=False)
#     id_number = db.Column(db.Integer, unique=True, nullable=False)
#     kra_pin = db.Column(db.String(13), unique=True, nullable=False)
#     birth = db.Column(db.Integer, nullable=False)
#     gender = db.Column(db.String(100), nullable=False)
#     mobile = db.Column(db.String(100), unique=True, nullable=False)
#     location = db.Column(db.String(100), nullable=False)
#     profession = db.Column(db.String(100), nullable=False)
#     employer = db.Column(db.String(100), nullable=False)
#     qualification = db.Column(db.String(50), nullable=False)
#     role = db.Column(db.String(20), nullable=False, default='user')
#     cv = db.Column(db.String(100), nullable=False)
#     id_card = db.Column(db.String(100), nullable=False)
#     is_verified = db.Column(db.String(10), nullable=False, default=False)
#     password = db.Column(db.String(100), nullable=False)
#     date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     jobs_done = db.relationship('Jobs', secondary='workers', backref=db.backref('worker'), lazy='dynamic')
#
#     # def __repr__(self):
#     # return f"{self.name}, {self.location}, {self.profession}"
#
#     def get_reset_token(self, expires_sec=1800):
#         s = Serializer(app.config['SECRET_KEY'], expires_sec)
#         return s.dumps({'user_id': self.user_id}).decode('utf-8')
#
#     @staticmethod
#     def verify_reset_token(token):
#         s = Serializer(app.config['SECRET_KEY'])
#         try:
#             user_id = s.loads(token)['user_id']
#         except:
#             return None
#         return User.query.get(user_id)
#
#
# class Employers(db.Model, UserMixin):
#
#     __tablename__ = 'employers'
#
#     def get_id(self):
#         return self.client_id
#
#     client_id = db.Column(db.Integer, primary_key=True)
#     employer_Name = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), unique=True, nullable=False)
#     kra_pin = db.Column(db.String(13), unique=True, nullable=False)
#     business_registration_number = db.Column(db.String(100), unique=True, nullable=False)
#     postal_address = db.Column(db.String(100), unique=True, nullable=False)
#     town = db.Column(db.String(100), nullable=False)
#     county = db.Column(db.String(100), nullable=False)
#     physical_address = db.Column(db.String(100), nullable=False)
#     mobile = db.Column(db.String(15), unique=True, nullable=False)
#     website = db.Column(db.String(100), unique=True, nullable=False)
#     economic_activity = db.Column(db.String(100), unique=True, nullable=False)
#     password = db.Column(db.String(100), nullable=False)
#     date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#
#     def get_reset_token(self, expires_sec=1800):
#         s = Serializer(app.config['SECRET_KEY'], expires_sec)
#         return s.dumps({'employer_id': self.id}).decode('utf-8')
#
#     @staticmethod
#     def verify_reset_token(token):
#         s = Serializer(app.config['SECRET_KEY'])
#         try:
#             employer_id = s.loads(token)['employer_id']
#         except:
#             return None
#         return Employers.query.get(employer_id)
#
#     def __repr__(self):
#         return f"{self.employer_Name}, {self.email}, {self.business_registration_number}, {self.date_created}"
#
#
# class Jobs(db.Model):
#
#     __tablename__ = 'jobs'
#     job_id = db.Column(db.Integer, primary_key=True)
#     job_title = db.Column(db.String(200), nullable=False)
#     company_name = db.Column(db.String(100), nullable=False)
#     date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     job_location = db.Column(db.String(100), nullable=False)
#     no_of_workers = db.Column(db.Integer, nullable=False)
#     job_rating = db.Column(db.Integer, nullable=False, default=0)
#     job_info_file = db.Column(db.String(100), nullable=False)
#     created_by = db.Column(db.String(100), nullable=False)
#
#
# class MyModelView(ModelView):
#     column_exclude_list = ['password', 'image_file']
#     can_delete = False  # disable model deletion
#     can_create = False
#     column_searchable_list = ('name', 'id_number', 'profession', 'location')
#     can_export = True
#     page_size = 50
#
#     def is_accessible(self):
#         # Use the role column to determine who accesses the page
#         if current_user.role == 'admin':
#             return current_user.is_authenticated
#         else:
#             return abort(404)
#
#     def not_auth(self):
#         return "You are not authorized to use admin page"
#
#
# class JobsModelView(ModelView):
#     can_delete = False  # disable model deletion
#     can_create = False
#     can_edit = True
#     can_export = True
#     page_size = 50
#
#     def is_accessible(self):
#         # Use the role column to determine who accesses the page
#         if current_user.role == 'admin':
#             return current_user.is_authenticated
#         else:
#             return abort(404)
#
#     def not_auth(self):
#         return "You are not authorized to use admin page"
#
#
# class EmployersModelView(ModelView):
#     can_delete = False  # disable model deletion
#     can_create = False
#     can_edit = True
#     can_export = True
#     page_size = 50
#
#     def is_accessible(self):
#         # Use the role column to determine who accesses the page
#         if current_user.role == 'admin':
#             return current_user.is_authenticated
#         else:
#             return abort(404)
#
#     def not_auth(self):
#         return "You are not authorized to use admin page"
#
#
# admin.add_view(MyModelView(User, db.session))
# admin.add_view(EmployersModelView(Employers, db.session))
# admin.add_view(JobsModelView(Jobs, db.session))
#
#
#
