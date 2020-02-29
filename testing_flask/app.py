import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


# Create the flask app
app = Flask(__name__)


# How should the app connect to your db?
# This is nice and quick for local testing
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# But use this one when you deploy to heroku
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")


# Makes sqlalchemy library/connection easy to use throughout the app
db = SQLAlchemy(app)

class FormResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Code_name = db.Column(db.String)
    Prioritising_workload = db.Column(db.Integer)
    Writing_notes = db.Column(db.Integer)
    Thinking_ahead = db.Column(db.Integer)
    Reliability = db.Column(db.Integer)
    Keeping_promises = db.Column(db.Integer)
    Funniness = db.Column(db.Integer)
    Criminal_damage = db.Column(db.Integer)
    Elections = db.Column(db.Integer)
    Self_criticism = db.Column(db.Integer)
    Empathy = db.Column(db.Integer)
    Eating_to_survive = db.Column(db.Integer)
    Giving = db.Column(db.Integer)
    Compassion_to_animals = db.Column(db.Integer)
    Borrowed_stuff = db.Column(db.Integer)
    Loneliness = db.Column(db.Integer)
    Cheating_in_school = db.Column(db.Integer)
    Health = db.Column(db.Integer)
    God = db.Column(db.Integer)
    Charity = db.Column(db.Integer)
    Number_of_friends = db.Column(db.Integer)
    Waiting = db.Column(db.Integer)
    Mood_swings = db.Column(db.Integer)
    Appearence_and_gestures = db.Column(db.Integer)
    Socializing = db.Column(db.Integer)
    Children = db.Column(db.Integer)
    Getting_angry = db.Column(db.Integer)
    Knowing_the_right_people = db.Column(db.Integer)
    Public_speaking = db.Column(db.Integer)
    Unpopularity = db.Column(db.Integer)
    Life_struggles = db.Column(db.Integer)
    Happiness_in_life = db.Column(db.Integer)
    Energy_levels = db.Column(db.Integer)
    Personality = db.Column(db.Integer)
    Finding_lost_valuables = db.Column(db.Integer)
    Getting_up = db.Column(db.Integer)
    Interests_or_hobbies = db.Column(db.Integer)
    Questionnaires_or_polls = db.Column(db.Integer)


    def __repr__(self):
        return '<FormResponse %r>' % self.id


# You probably do not want to drop data once you deploy, but if you're
# Having issues while changing the model attributes this may be helpful
db.drop_all()
# Have sqlalchemy create your db tables based on your Models
db.create_all()


@app.route('/',methods = ['GET'])
def form():
    """
    Display the form page
    """
    return render_template('index.html')


@app.route('/result',methods = ['POST'])
def result():
    """
    Accepts form data and stores it
    """
    result = request.form
    print(result) # Sanity check; can be removed when you know it works

    # If you rename the 'name' values in your html to match the
    # model fields, you can do this more simply as:
    #fr = FormResponse(**result)
    # Otherwise map your column names to html input names like this:
    fr = FormResponse(
        Code_name=result["Code_name"],
        Prioritising_workload=result["Prioritising_workload"],
        Writing_notes=result["Writing_notes"],
        Thinking_ahead=result["Thinking_ahead"],
        Reliability=result["Reliability"],
        Keeping_promises=result["Keeping_promises"],
        Funniness=result["Funniness"],
        Criminal_damage=result["Criminal_damage"],
        Elections=result["Elections"],
        Self_criticism=result["Self_criticism"],
        Empathy=result["Empathy"],
        Eating_to_survive=result["Eating_to_survive"],
        Giving=result["Giving"],
        Compassion_to_animals=result["Compassion_to_animals"],
        Borrowed_stuff=result["Borrowed_stuff"],
        Loneliness=result["Loneliness"],
        Cheating_in_school=result["Cheating_in_school"],
        Health=result["Health"],
        God=result["God"],
        Charity=result["Charity"],
        Number_of_friends=result["Number_of_friends"],
        Waiting=result["Waiting"],
        Mood_swings=result["Mood_swings"],
        Appearence_and_gestures=result["Appearence_and_gestures"],
        Socializing=result["Socializing"],
        Children=result["Children"],
        Getting_angry=result["Getting_angry"],
        Knowing_the_right_people=result["Knowing_the_right_people"],
        Public_speaking=result["Public_speaking"],
        Unpopularity=result["Unpopularity"],
        Life_struggles=result["Life_struggles"],
        Happiness_in_life=result["Happiness_in_life"],
        Energy_levels=result["Energy_levels"],
        Personality=result["Personality"],
        Finding_lost_valuables=result["Finding_lost_valuables"],
        Getting_up=result["Getting_up"],
        Interests_or_hobbies=result["Interests_or_hobbies"],
        Questionnaires_or_polls=result["Questionnaires_or_polls"]
        )

    # Save this response to your table
    db.session.add(fr)
    db.session.commit()

    # Another sanity check
    result_set = FormResponse.query.all()
    print(result_set)

    # Send your user back to the form page or another page if you like
    return redirect('/')

if __name__ == '__main__':
    # You probably don't want debug=True in your final deploy
    app.run(debug = True)