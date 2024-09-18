from data_pipeline.extraction import extract
from data_pipeline.processing import processing
from data_pipeline.loading import load
import pandas as pd
from sqlalchemy import *

#connect with your database:
engine = create_engine('postgresql://postgres:password@localhost/games')


#Defining endpoints and extracting
def extraction_task():
    raw_games = extract('games') #endpoint
    raw_genre = extract('genres')
    return raw_games, raw_genre


# PROCESSING DATA
#filter the columns to the ones that match your model, drop duplicates and check null values
def processing_task(raw_games, raw_genre):
    cleaned_games = processing(raw_games)
    cleaned_genre = processing(raw_genre)

    cleaned_games['first_release_date'] = pd.to_datetime(cleaned_games['first_release_date'], unit='s')

    cleaned_genre = raw_genre[['id', 'name']]
    cleaned_genre = cleaned_genre.sort_values(by='id')
    return cleaned_genre, cleaned_games


def loading_task(cleaned_games, cleaned_genre):
    load(cleaned_games, cleaned_genre)
