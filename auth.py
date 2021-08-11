import json
import random
import tweepy

# Loading tracks from the JSON file into a list
f = open('Lyrics_InsideTheSongs.json')
tracks = json.load(f)['tracks']

# Creating a list of tuples viz. (SONG NAME, SONG LYRICS)
album= []
for track in tracks:
    name = track['song']['title']
    words = track['song']['lyrics']
    album.append((name, words))

# Function definitions 
def pick_random_song(album):
    n = len(album)
    index = random.randint(0,n-1)
    song = album[index]
    return song[1]

def pick_random_line(lyrics):
    arr1 = lyrics.split('\n') 
    
    arr2 = [line for line in arr1 if line != '']
    
    arr = [line for line in arr2 if line[0] != '[']
    
    no_of_lines = random.randint(0,4)
    index = random.randint(0,len(arr)-no_of_lines) 
    line = '\n'.join(arr[index:index+no_of_lines])
        
    return line
    

# Configuring Twitter API

consumer_key = ''' ENTER YOUR CONSUMER KEY HERE'''
consumer_secret =  ''' ENTER YOUR CONSUMER SECRET HERE '''

bearer_token = ''' ENTER YOUR BEARER TOKEN HERE '''
access_token = ''' ENTER YOUR ACCESS TOKEN HERE '''
access_token_secret = ''' ENTER YOUR ACCESS TOKEN SECRET HERE '''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
