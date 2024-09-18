import pandas as pd
from sqlalchemy import *

def load(cleaned_games, cleaned_genre):
    #joining both tables
    joined_tb = pd.merge(cleaned_games, cleaned_genre, how='left', left_on='genres', right_on='id')

    #adjusting data types
    joined_tb = joined_tb.drop(columns=['genres', 'id_y'])
    joined_tb = joined_tb.rename(columns={'name_y':'genre'})
    joined_tb = joined_tb.rename(columns={'id_x':'game_id'})
    joined_tb = joined_tb.rename(columns={'name_x':'name'})
    joined_tb['game_id'] = joined_tb['game_id'].astype(int)
    joined_tb['name'] = joined_tb['name'].astype(str)
    joined_tb['genre'] = joined_tb['genre'].astype(str)


    # LOADING TO DATABASE
    joined_tb.to_sql('staging_games', engine, if_exists='replace', index=False)
    print('Data loaded into staging table')


    #joining staging with main table:
    join_query = text('''
    INSERT INTO games (game_id, name, first_release_date, genre)
    SELECT s.game_id, s.name, s.first_release_date, s.genre
    FROM staging_games s
    LEFT JOIN games g 
    ON s.game_id = g.game_id 
    AND s.name = g.name 
    AND s.first_release_date = g.first_release_date 
    AND s.genre = g.genre
    WHERE g.game_id IS NULL 
    AND g.name IS NULL 
    AND g.first_release_date IS NULL 
    AND g.genre IS NULL;''')

    with engine.connect() as conn:
        conn.execute(join_query)
        conn.commit()
        print('Data merged into main table')

    # Cleaning staging table
        truncate_query = text("TRUNCATE TABLE staging_games;")
        conn.execute(truncate_query)
        conn.commit()
        print('Staging table truncated')