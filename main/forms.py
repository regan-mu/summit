# from flask_wtf import FlaskForm
# from flask_login import current_user
# from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
# from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
# from password_strength import PasswordPolicy, PasswordStats
# # from main.models import User, Employers
#
#
# # Student Registration Form
# class Registration(FlaskForm):
#     courses = ['Data Analysis with Python', 'Python Programming']
#     adverts = ['Facebook', 'Instagram', 'Twitter', 'Youtube Ads', 'Google Search', 'Friend', 'Other']
#     qualify = ['-- Level of Qualification --', 'PhD', 'Masters', 'Degree', 'Diploma', 'Technician', 'Artisan']
#     fname = StringField('First Name', validators=[DataRequired(), Length(min=3, max=20)],
#                         render_kw={"placeholder": "First Name"})
#     lname = StringField('Last Name', validators=[DataRequired(), Length(min=3, max=20)],
#                         render_kw={"placeholder": "Last Name"})
#     email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
#     mobile = StringField('Mobile', validators=[DataRequired(), Length(min=0, max=20)],
#                          render_kw={"placeholder": "Mobile"})
#     gender = SelectField('Gender', validators=[DataRequired()], choices=['-- Gender --', 'Male', 'Female', 'Other'])
#     country = StringField('Country', validators=[DataRequired()])
#     course = SelectField('Course', validators=[DataRequired()], choices=courses)
#     educationLevel = SelectField('Education Level', validators=[DataRequired()], choices=qualify)
#     media = SelectField('How did you hear about us?', validators=[DataRequired()], choices=adverts)
#     password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=200)],
#                              render_kw={"placeholder": "Password"})
#     confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')],
#                                      render_kw={"placeholder": "Confirm Password"})
#     submit = SubmitField('Apply')
#
#     # Verification whether username exist in Db
#     def validate_email(self, email):
#         user = User.query.filter_by(email=email.data).first()
#         employer = Employers.query.filter_by(email=email.data).first()
#         if user or employer:
#             raise ValidationError('Email already exists')
#
#     # Verification whether ID Number exist in Db
#     def validate_id_number(self, id_number):
#         user = User.query.filter_by(id_number=id_number.data).first()
#         if user:
#             raise ValidationError('ID Number already exists! Please confirm.')
#
#     # Verification whether Mobile Number exist in Db
#     def validate_mobile(self, mobile):
#         user = User.query.filter_by(mobile=mobile.data).first()
#         if user:
#             raise ValidationError('Mobile Number already exists! Please confirm.')
#
#     # Verify KRA Pin
#     def validate_kra_pin(self, kra_pin):
#         user = User.query.filter_by(kra_pin=kra_pin.data).first()
#         if user:
#             raise ValidationError('KRA pin already exists! Please confirm.')
#
#     # Check password strength
#     def validate_password(self, password):
#         policy = PasswordPolicy.from_names(length=8, uppercase=1, numbers=1, special=1, strength=0.30)
#         password = password.data
#         stats = PasswordStats(password)
#         checkpolicy = policy.test(password)
#         if stats.strength() < 0.30:
#             raise ValidationError('Password too weak! Avoid consecutive characters and easily guessed numbers!')
#
#
# # Student Login form
# class Login(FlaskForm):
#     email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
#     password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=200)], render_kw={"placeholder": "Password"})
#     remember = BooleanField('Remember me')
#     submit = SubmitField('Login')
#
#
# # Student password reset request
# class RequestReset(FlaskForm):
#     email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
#     submit = SubmitField('Request Password Reset')
#
#     # Check whether the email address is already in the database
#     def validate_email(self, email):
#         user = User.query.filter_by(email=email.data).first()
#         if user is None:
#             raise ValidationError(f'{email.data} does not exist!')
#
#
# # Student Reset password expert
# class ResetPassword(FlaskForm):
#     password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=200)], render_kw={"placeholder": "Password"})
#     confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "Confirm Password"})
#     submit = SubmitField('Reset')
#
#     def validate_password(self, password):
#         policy = PasswordPolicy.from_names(length=8, uppercase=1, numbers=1, special=1, strength=0.66)
#         password = password.data
#         stats = PasswordStats(password)
#         checkpolicy = policy.test(password)
#         if stats.strength() < 0.30:
#             raise ValidationError('Password too weak! Avoid consecutive characters and easily guessed numbers!')
#
#
# # Update Student Info
# class Update(FlaskForm):
#     qualify = ['-- Level of Qualification --', 'PhD', 'Masters', 'Degree', 'Diploma', 'Technician', 'Artisan']
#     email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
#     mobile = StringField('Mobile Number', validators=[DataRequired(), Length(min=0, max=20)],
#                          render_kw={"placeholder": "Mobile"})
#     educationLevel = SelectField('Education Level', validators=[DataRequired()], choices=qualify)
#     submit = SubmitField('Update')
#
#     # Verification whether email exist in Db
#     def validate_email(self, email):
#         if email.data != current_user.email:
#             user = User.query.filter_by(email=email.data).first()
#             if user:
#                 raise ValidationError('Email already exists')
#
#     # Verification whether Mobile Number exist in Db
#     def validate_mobile(self, mobile):
#         if mobile.data != current_user.mobile:
#             user = User.query.filter_by(mobile=mobile.data).first()
#             if user:
#                 raise ValidationError('Mobile Number already exists! Please confirm.')
#
#
# # Create new Cohort
# class Cohorts(FlaskForm):
#     cohortTitle = StringField('Cohort Title', validators=[DataRequired()])
#     Course = StringField('Course', validators=[DataRequired()])
#     taughtBy = StringField('Taught By', validators=[DataRequired()])
#     submit = SubmitField('New Cohort')
#
