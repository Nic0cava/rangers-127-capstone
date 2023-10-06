from werkzeug.security import generate_password_hash #check_password_hash #allows us to generate a hashed password
from flask_sqlalchemy import SQLAlchemy #allows our database to read our classes/objects as tables/rows 
from flask_login import UserMixin, LoginManager, current_user#allows us to load a current logged in user
from datetime import datetime
import uuid #generate a unique id
from flask_marshmallow import Marshmallow 



#internal import
from .helpers import get_image


db = SQLAlchemy() #instantiate our database
login_manager = LoginManager() #instantiate our login manager
ma = Marshmallow() #instantiating our Marshmallow class 


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id) #this queries our database & brings back the user with the same id


class User(db.Model, UserMixin):
    #think of this part as the CREATE TABLE 'User' 
    user_id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    date_added = db.Column(db.DateTime, default = datetime.utcnow)
    goal = db.relationship('Goal', backref='user', lazy = True) # stores all goals per user

    #think of our __init__() as our INSERT INTO 
    def __init__(self, username, email, password, first_name="", last_name=""):
        self.user_id = self.set_id() #method to create a unique id
        self.first_name = first_name
        self.last_name = last_name 
        self.username = username
        self.email = email
        self.password = self.set_password(password) #method to hash our password for security 


    def set_id(self):
        return str(uuid.uuid4())
    

    def get_id(self):
        return str(self.user_id)
    

    def set_password(self, password):
        return generate_password_hash(password)
    

    def __repr__(self):
        return f"<USER: {self.username}"
    



class Goal(db.Model):
    goal_id = db.Column(db.String, primary_key = True)
    goal_name = db.Column(db.String(100), nullable = False)
    reward = db.Column(db.String(500), nullable = False) #image
    action1 = db.Column(db.String(100)) # actions are optional
    action2 = db.Column(db.String(100))
    action3 = db.Column(db.String(100))
    action4 = db.Column(db.String(100))
    action5 = db.Column(db.String(100))
    date_added = db.Column(db.DateTime, default = datetime.utcnow)
    # ForeignKey
    user_id = db.Column(db.String, db.ForeignKey('user.user_id'), nullable = False) # one to many relationship


    def __init__(self, goal_name, reward, action1="", action2="", action3="", action4="", action5=""):
        self.goal_id = self.set_id()
        self.goal_name = goal_name
        self.reward = self.set_reward(reward)
        self.user_id = current_user.user_id
        self.action1 = action1
        self.action2 = action2
        self.action3 = action3
        self.action4 = action4
        self.action5 = action5

    def set_id(self):
        return str(uuid.uuid4()) #create unique ID 
    
    def set_reward(self, reward):
        image = get_image(reward) #adding get_image function which makes an external 3rd party API callh
        print("api image", image)
        return image
    

    def __repr__(self):
        return f"<GOAL: {self.goal_name}>"
    



#Building Schema
#How object looks when being passed from server to server 
#These will look like dictionaries 



class GoalSchema(ma.Schema):
    class Meta: 
        fields = ['goal_id', 'goal_name', 'reward', 'action1', 'action2', 'action3', 'action4', 'action5'] 



goal_schema = GoalSchema() #this is for passing 1 singular product 
goals_schema = GoalSchema(many = True) #this for passing multiple products, list of dictionaries 




    
