from flask import Blueprint, render_template, request, flash, redirect
from flask_login import current_user

#internal imports
from capstone.models import Goal, db, goal_schema, goals_schema 
from capstone.forms import GoalForm
from capstone.helpers import get_quote




#instantiate our Blueprint object
site = Blueprint('site', __name__, template_folder='site_templates') #telling your blueprint where to load the html files



@site.route('/')
def home():

    #home = Goal.query.all() #grabbing all the goals
    home = []
    if current_user.is_authenticated:

        home = Goal.query.filter(Goal.user_id == current_user.user_id).all() #trying to grab goals on that specific user
    # data = get_quote()
    # quote = data[0]
    # author = data[1]


    return render_template('home.html', home=home)



#create CREATE route
@site.route('/home/create', methods = ['GET', 'POST'])
def create():

    createform = GoalForm()

    if request.method == 'POST' and createform.validate_on_submit():

        try: 
            goal_name = createform.goal_name.data
            reward = createform.reward.data
            action1 = createform.action1.data
            action2 = createform.action2.data
            action3 = createform.action3.data
            action4 = createform.action4.data
            action5 = createform.action5.data
            # user_id = Goal.user_id
            # user_id = current_user

            goal = Goal(goal_name, reward,  action1, action2, action3, action4, action5) #instantiating Goal object

            db.session.add(goal)
            db.session.commit()

            flash(f"You have successfully created goal {goal_name}", category='success')
            return redirect('/')
        
        except:
            flash("We were unable to process your request. Please try again", category='warning')
            return redirect('/home/create')
        
        
    return render_template('create.html', form=createform)



#create UPDATE route
@site.route('/home/update/<id>', methods = ['GET', 'POST'])
def update(id):

    updateform = GoalForm()
    goal = Goal.query.get(id) #WHERE clause WHERE goal.goal_id == id 

    if request.method == 'POST' and updateform.validate_on_submit():

        try: 
            goal.goal_name = updateform.goal_name.data
            goal.set_reward(updateform.reward.data) #calling upon set_reward method to set image!
            goal.action1 = updateform.action1.data
            goal.action2 = updateform.action2.data
            goal.action3 = updateform.action3.data
            goal.action4 = updateform.action4.data
            goal.action5 = updateform.action5.data

            

            db.session.commit() 

            flash(f"You have successfully updated goal {goal.goal_name}", category='success')
            return redirect('/')

        except:
            flash("We were unable to process your request. Please try again", category='warning')
            return redirect('/home/update')
        
    return render_template('update.html', form=updateform, goal=goal)


#create DELETE route
@site.route('/home/delete/<id>')
def delete(id):

    goal = Goal.query.get(id)

    db.session.delete(goal)
    db.session.commit()

    return redirect('/')
