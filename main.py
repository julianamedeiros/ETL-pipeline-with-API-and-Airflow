from data_pipeline.extraction import ext
import pandas as pd
import sqlalchemy


#Defining endpoints and extracting
raw_games = ext('games')
raw_genre = ext('genres')


#model and process data
#filter the columns to the ones that match your model, drop duplicates and check null values

cleaned_games = raw_games[['id', 'name', 'first_release_date', 'genres']]
cleaned_games = cleaned_games.explode('genres')
cleaned_games = cleaned_games.dropna()
cleaned_games = cleaned_games.sort_values(by='id')

cleaned_games['first_release_date'] = pd.to_datetime(cleaned_games['first_release_date'], unit='s')

cleaned_genre = raw_genre[['id', 'name']]
cleaned_genre = cleaned_genre.sort_values(by='id')

#joining both tables

joined_tb = pd.merge(cleaned_games, cleaned_genre, how='left', left_on='genres', right_on='id')
joined_tb = joined_tb.drop(columns=['genres', 'id_y'])
joined_tb = joined_tb.rename(columns={'name_y':'genre'})

#load to database

