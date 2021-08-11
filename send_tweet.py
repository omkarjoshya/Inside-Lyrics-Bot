import auth
import tweepy

def job():
    # the entire authentication flow is completed by calling the .API() method
    api = tweepy.API(auth.auth)
    # setting the album variable
    album = auth.album
    try:
        lyric = auth.pick_random_line(auth.pick_random_song(album))
        api.update_status(lyric)
        print((lyric))
    except Exception as e:
        print(f"Oops! {e.__class__}")

job()
