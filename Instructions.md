# Heroku Instructions

## Make sure you have the following
* requirements.txt
* Profile
* using DATABASE_URL environment variable
* all of these are commited

## Follow these steps
* `heroku create`
* `heroku addons:create heroku-postgresql:hobby-dev`
* `git push heroku master`