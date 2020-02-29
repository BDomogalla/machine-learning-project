# Import Modules & Dependencies
import sklearn
import tensorflow
import pandas as pd
import os

from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from tensorflow.keras.models import load_model
from sklearn.externals import joblib

all_features_df = pd.read_csv("filesource")

snakes_features_df = all_features_df[["Thinking ahead", "Health", "God", "Number of friends",
                                      "Children", "Getting angry", "Public speaking"]]

spiders_features_df = all_features_df[["Number of friends", "Appearance and gestures", "Children", "Getting angry", "Public speaking",
                                       "Unpopularity", "Life struggles", "Happiness in life", "Getting up", "Questionnaires or polls"]]

heights_features_df = all_features_df[["Funniness", "Self-criticism", "Eating to survive", "Loneliness", "Health", "Waiting",
                                       "Appearance and gestures", "Knowing the right people", "Life struggles", "Energy levels"]]

gender_features_df = all_features_df[["Prioritizing workload", "Writing notes", "Reliability", "Keeping promises", "Funniness", "Criminal damage",
                                      "Empathy", "Eating to survive", "Giving", "Compassion to animals", "Mood swings", "Socializing", "Life struggles",
                                      "Personality", "Interests or hobbies", "Questionnaires or polls"]]

education_features_df = all_features_df[["Elections", "Borrowed stuff", "Cheating in school", "God", "Charity", "Waiting", "Appearance and gestures",
                                         "Happiness to life", "Personality", "Finding lost valuables"]]



def snakes_func():

    # Define the Features (X) to be Used in the Model
    X = snakes_features_df
    y = all_features_df["Snakes"]

    # Create a MinMaxScaler Model and Fit it to the X values
    X_scaler = MinMaxScaler().fit(X)

    # Transform the Data Using the X_Scaler
    X_scaled = X_scaler.transform(X)

    # Label-Encode Data
    label_encoder = LabelEncoder()
    label_encoder.fit(y)
    encoded_y = label_encoder.transform(y)

    # Load the model
    snakes_model = load_model("models/Best_models/snakes_NN_model.h5")

    # Use Model to Predict Target
    snakes_prediction = snakes_model.predict_classes(X_scaled)
    prediction_label = label_encoder.inverse_transform(snakes_prediction)

    return print(f"Predicted Fear of Snakes: {prediction_label}")



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