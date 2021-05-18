import pandas as pd
import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.tree import export_graphviz
# import pydot
# import csv
import joblib
from keras.models import load_model
from keras.preprocessing import sequence
import pickle

def Rating_prediction(year,duration,nrOfGenre,Genre):
    #default
    gen_text = 'Action, Adult, Adventure, Animation, Biography, Comedy, Crime, Documentary, Drama, Family, Fantasy, FilmNoir, GameShow, History, Horror, Music, Musical, Mystery, News, RealityTV, Romance, SciFi, Short, Sport, TalkShow, Thriller, War, Western'
    data_default = {'duration':[3600],
    'year':[2010],
    'nrOfGenre':[28],
    'genre':[gen_text]}
    # Create DataFrame
    df = pd.DataFrame(data_default)

    # new data
    Genre = Genre + ','
    duration = int(duration)*60
    new_row = {'duration':duration, 'year':year, 'nrOfGenre':nrOfGenre, 'genre':Genre}
    #append row to the dataframe
    df = df.append(new_row, ignore_index=True)
    # get_dummies genre
    final_data = pd.concat([df, df['genre'].str.get_dummies(sep=' ')], axis=1)
    final_data = final_data.drop(columns='genre')
    input_data = final_data.iloc()[1].values

    #Prediction
    loaded_rf = joblib.load("model/rating_random_forest.joblib")
    rating = loaded_rf.predict([input_data])
    return rating[0]

def descript_rating_prediction(text):

    maxlen = 250
    max_word = 10000
    with open('model/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    # Preprocess data 
    sequeces = tokenizer.texts_to_sequences([text])
    padding_sequences = sequence.pad_sequences(sequeces,maxlen = maxlen)

    # load model
    model_lstm = load_model('model/lstm_model.h5')

    # predict
    pred_class = model_lstm.predict(padding_sequences).argmax(axis =1)
    label_to_score_class = [0,1,2,3,4,5,6,7,8,9]
    result = label_to_score_class[int(pred_class)]

    return result+1