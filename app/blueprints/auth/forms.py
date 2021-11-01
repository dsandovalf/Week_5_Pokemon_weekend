from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import Email, DataRequired, EqualTo, ValidationError
from app.models import User
from jinja2 import Markup
import random

class LoginForm(FlaskForm):
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


    r1=random.randint(1,37)
    r2=random.randint(38,75)
    r3=random.randint(76,113)
    r4=random.randint(114,151)
    # video 2:13
    r1_image=Markup(f'<img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/{r1}.gif" style="height:75px">')
    r2_image=Markup(f'<img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/{r2}.gif" style="height:75px">')
    r3_image=Markup(f'<img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/{r3}.gif" style="height:75px">')
    r4_image=Markup(f'<img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/{r4}.gif" style="height:75px">')

    icon = RadioField('Choose your starter Pokemon',
        choices=[(r1,r1_image),(r2,r2_image),(r3,r3_image),(r4,r4_image)],
        validators=[DataRequired()])


        # MUST BE LIKE THIS VALIDATE_FIELDNAME
    def validate_email(form, field):                               #give me only the first result returns 1 user object
        same_email_user = User.query.filter_by(email = field.data).first()
                        # SELECT * FROM user WHERE email = ???
                        # filter_by always gives a list
        if same_email_user:
            raise ValidationError("Email is already in use")

class EditProfileForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


    r1=random.randint(1,37)
    r2=random.randint(38,75)
    r3=random.randint(76,113)
    r4=random.randint(114,151)
    # video 2:13
    r1_image=Markup(f'<img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/{r1}.gif" style="height:75px">')
    r2_image=Markup(f'<img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/{r2}.gif" style="height:75px">')
    r3_image=Markup(f'<img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/{r3}.gif" style="height:75px">')
    r4_image=Markup(f'<img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/{r4}.gif" style="height:75px">')

    icon = RadioField('Choose your starter Pokemon',
        choices=[(9000,"Don't Change"),(r1,r1_image),(r2,r2_image),(r3,r3_image),(r4,r4_image)],
        validators=[DataRequired()])

