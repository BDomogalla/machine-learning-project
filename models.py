# Import Modules & Dependencies
import sklearn
import tensorflow
import pandas as pd
import os

from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from tensorflow.keras.models import load_model
from sklearn.externals import joblib

all_features_df = pd.read_csv("filesource")

snakes_features_df = all_features_df[["Thinking_ahead", "Health", "God", "Number_of_friends",
                                      "Children", "Getting_angry", "Public_speaking"]]

spiders_features_df = all_features_df[["Number_of_friends", "Appearance_and_gestures", "Children", "Getting_angry", "Public_speaking",
                                       "Unpopularity", "Life_struggles", "Happiness_in_life", "Getting_up", "Questionnaires_or_polls"]]

heights_features_df = all_features_df[["Funniness", "Self_criticism", "Eating_to_survive", "Loneliness", "Health", "Waiting",
                                       "Appearance_and_gestures", "Knowing_the_right_people", "Life_struggles", "Energy_levels"]]

gender_features_df = all_features_df[["Prioritising_workload", "Writing_notes", "Reliability", "Keeping_promises", "Funniness", "Criminal_damage",
                                      "Empathy", "Eating_to_survive", "Giving", "Compassion_to_animals", "Mood_swings", "Socializing", "Life_struggles",
                                      "Personality", "Interests_or_hobbies", "Questionnaires_or_polls"]]

education_features_df = all_features_df[["Elections", "Borrowed_stuff", "Cheating_in_school", "God", "Charity", "Waiting", "Appearance_and_gestures",
                                         "Happiness_in_life", "Personality", "Finding_lost_valuables"]]



def snakes_func():

    # Define the Features (X) to be Used in the Model
    X = snakes_features_df

    # Create a MinMaxScaler Model and Fit it to the X values
    X_scaler = MinMaxScaler().fit(X)

    # Transform the Data Using the X_Scaler
    X_scaled = X_scaler.transform(X)

    # Load the model
    snakes_model = load_model("models/Best_models/snakes_NN_model.h5")

    # Use Model to Predict Target
    snakes_prediction = snakes_model.predict_classes(X_scaled)

    def prediction_translator():

        if snakes_prediction == 2:
            return "Not Afraid"

        elif snakes_prediction == 1:
            return "Neutral"

        else:
            return "Afraid"

        return print(f"Predicted Fear of Snakes: {prediction_translator(snakes_prediction)}")



def spiders_func():

    # Define the Features (X) and to be Used in the Model
    X = spiders_features_df

    # Create a MinMaxScaler Model and Fit it to the X values
    X_scaler = MinMaxScaler().fit(X)

    # Transform the Data Using the X_Scaler
    X_scaled = X_scaler.transform(X)

    # Load the model
    spiders_model = joblib.load("models/Best_models/spiders_Logit_model.sav")

    # Use Model to Predict Target
    spiders_prediction = spiders_model.predict(X_scaled)

    return print(f"Predicted Fear of Spiders: {spiders_prediction}")

    

def heights_func():

    # Define the Features (X) to be Used in the Model
    X = heights_features_df

    # Load the model
    heights_model = joblib.load("models/Best_models/heights_KNN_model.sav")

    # Use Model to Predict Target
    heights_prediction = heights_model.predict(X)

    return print(f"Predicted Fear of Heights: {heights_prediction}")



def education_func():

    # Define the Features (X) and to be Used in the Model
    X = education_features_df

    # Load the model
    education_model = joblib.load("models/Best_models/education_KNN_model.sav")

    # Use Model to Predict Target
    education_prediction = education_model.predict(X)

    return print(f"Predicted Education Level: {education_prediction}")



def gender_func():

    # Define the Features (X) and to be Used in the Model
    X = gender_features_df

    # Load the model
    gender_model = joblib.load("models/Best_models/gender_KNN_model.sav")

    # Use Model to Predict Target
    gender_prediction = gender_model.predict(X)

    return print(f"Predicted Gender: {gender_prediction}")



snakes_func()
spiders_func()
heights_func()
education_func()
gender_func()