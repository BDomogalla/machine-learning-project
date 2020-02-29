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
    prioritising_workload = db.Column(db.Integer)
    keeping_promises = db.Column(db.Integer)

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
    # fr = FormResponse(**result)
    # Otherwise map your column names to html input names like this:
    fr = FormResponse(
        prioritising_workload=result["Prioritising workload"],
        keeping_promises=result["Keeping promises"]
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