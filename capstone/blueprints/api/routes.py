from flask import Blueprint, request, jsonify 
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity 

#internal imports 
from capstone.models import Goal, db, goal_schema, goals_schema 


#instantiate our blueprint
api = Blueprint('api', __name__, url_prefix = '/api') #all of our endpoints need to be prefixed with /api



@api.route('/token', methods = ['GET', 'POST'])
def token():

    data = request.json

    if data:
        client_id = data['client_id'] #looking for the key of client_id on the dictionary passed to us
        access_token = create_access_token(identity=client_id) 
        return {
            'status' : 200,
            'access_token' : access_token 
        }
    
    else:
        return {
            'status': 400,
            'message': 'Missing Client Id. Try Again'
        }
    

#creating our READ data request for home
@api.route('/')
@jwt_required()
def get_shop():

    home = Goal.query.all() #list of objects, we can't send a list of objects through api calls 

    response = goals_schema.dump(home) #takes our list of objects and turns it into a list of dictionaries 
    return jsonify(response) #jsonify essentially stringifies the list to send to our frontend 

    

