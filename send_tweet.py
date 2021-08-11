import auth
import tweepy


def job():
    api = tweepy.API(auth.auth)
    album = auth.album
    try:
        lyric = auth.pick_random_line(auth.pick_random_song(album))
        api.update_status(lyric)
        print((lyric))
    except Exception as e:
        print(f"Oops! {e.__class__}")

job()
