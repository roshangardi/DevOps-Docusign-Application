from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, ValidationError, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Requestor (R)', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('R Email', validators=[DataRequired(), Email()])
    # password = PasswordField('Password', validators=[DataRequired()])
    # confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    vusername = StringField('Division  Vice President (DVP)', validators=[DataRequired(), Length(min=2, max=20)])
    vemail = StringField('DVP Email', validators=[DataRequired(), Email()])
    submit = SubmitField('get eSign')

# class LoginForm(FlaskForm):
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     remember = BooleanField('Remember Me')
#     submit = SubmitField('Login')

