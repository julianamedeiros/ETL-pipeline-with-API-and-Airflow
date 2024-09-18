import pandas as pd

def processing(raw_games, raw_genre):
    cleaned_games = raw_games[['id', 'name', 'first_release_date', 'genres']]
    cleaned_games = cleaned_games.explode('genres')
    cleaned_games = cleaned_games.dropna()
    cleaned_games = cleaned_games.sort_values(by='id')

    cleaned_games['first_release_date'] = pd.to_datetime(cleaned_games['first_release_date'], unit='s')

    cleaned_genre = raw_genre[['id', 'name']]
    cleaned_genre = cleaned_genre.sort_values(by='id')
    return cleaned_genre, cleaned_games