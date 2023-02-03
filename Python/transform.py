from extract import extraction
import pandas as pd 

def transformation():
    album_df,artist_df,songs_df = extraction()
    album_df= album_df.drop_duplicates(subset='album_id')
    album_df['date_time']= pd.to_datetime(album_df['date_time'])

    artist_df = artist_df.drop_duplicates(subset='artist_id')

    songs_df['song_played_at'] = pd.to_datetime(songs_df['song_played_at'])
    songs_df['song_played_at']= songs_df['song_played_at'].dt.tz_convert('Asia/Kathmandu')
    songs_df['song_played_at']= songs_df['song_played_at'].astype(str).str[:-7]
    songs_df['song_played_at'] = pd.to_datetime(songs_df['song_played_at'])
    songs_df['UNIX_TIME']= (songs_df['song_played_at'] - pd.Timestamp("1970-01-01"))//pd.Timedelta('1s')
    songs_df['uid'] = songs_df['song_id'] + '-' + songs_df['UNIX_TIME'].astype(str)
    songs_df = songs_df[['uid','song_id','song_name','song_duration','song_url','song_popularity','song_played_at','song_album_id','song_artist_name']]
    album_df.to_csv('./albums.csv',index=False)
    artist_df.to_csv('./artist.csv',index=False)
    songs_df.to_csv('./song.csv',index=False) 
transformation()