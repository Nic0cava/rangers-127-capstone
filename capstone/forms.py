from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DecimalField
from wtforms.validators import DataRequired, EqualTo, Email 



#create Login form
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[ DataRequired(), Email() ])
    password = PasswordField('Password', validators = [ DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


#create Register Form
class RegisterForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    username = StringField('Username', validators=[ DataRequired() ])
    email = StringField('Email', validators=[ DataRequired(), Email() ])
    password = PasswordField('Password', validators = [ DataRequired()])
    verify_password = PasswordField('Confirm Password', validators=[ DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

#creat Goal Form
class GoalForm(FlaskForm):
    goal_name = StringField("Goal Name", validators=[ DataRequired()])
    reward = StringField("Reward", validators=[ DataRequired()])
    action1 = StringField("Action-1  **Optional")
    action2 = StringField("Action-2  **Optional")
    action3 = StringField("Action-3  **Optional")
    action4 = StringField("Action-4  **Optional")
    action5 = StringField("Action-5  **Optional")
    submit = SubmitField()