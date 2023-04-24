import requests
import bs4
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import smtplib
import os


class Send:
    
    def __init__(self):
        
        self.username = os.system.environ["username"]
        self.scope = 'playlist-modify-public'
        self.client_id = os.system.environ["id"]
        self.client_secret = os.system.environ["secret"]
        self.redirect_uri = "http://localhost:8888/callback"
    
    def get_info(self):
        
        self.date = ""
        self.ig = self.e_ig.get()
        
        if int(self.eday.get()) < 10 and int(self.emonth.get()) < 10:
            self.date = f"0{self.eyear.get()}-0{self.emonth.get()}-{self.eday.get()}"
            
        elif int(self.emonth.get()) < 10:
            self.date = f"{self.eyear.get()}-0{self.emonth.get()}-{self.eday.get()}"
        
        elif int(self.eday.get()) < 10:
            self.date = f"0{self.eyear.get()}-{self.emonth.get()}-{self.eday.get()}"
        
        
    
    def get_songs(self):
        
        url = f"https://www.billboard.com/charts/hot-100/{self.date}/"
        soup = bs4.BeautifulSoup(requests.get(url).text, "lxml")
        soup = soup.find_all("div", class_ = "o-chart-results-list-row-container")
        self.songs = [ b.find("h3").getText(strip = True) for b in soup]
        
        
    def create_spotify_list(self):
        
        self.auth_manager = SpotifyOAuth(self.client_id, self.client_secret,
        self.redirect_uri,scope = "playlist-modify-public")
        
        self.list_songs = spotipy.Spotify(auth_manager = self.auth_manager)
        
        self.list_songs.user_playlist_create(self.username, "The list obada made me",
        True, False, "created by obada")
    
    
    def add_songs_to_list(self):

        self.playlist_id = self.list_songs.user_playlists(self.username)["items"][0]["id"]
        self.tracks = [ self.list_songs.search(a, 1, type = "track")["tracks"]["items"][0]["uri"] for a in self.songs ]
        self.list_songs.user_playlist_add_tracks(self.username, self.playlist_id, self.tracks, 0)
        
        
    def send_via_mail(self):
        
        mail = "obadahpy@gmail.com"
        msg = f"""Subject:Spotify playlist\n\n
        here is the link of the spotify playlist i made it contains the top 100 tren songs
        for the date you wanted\n
        https://open.spotify.com/playlist/{self.list_songs.user_playlists(self.username)['items'][0]['id']}"""
        a = smtplib.SMTP("smtp.gmail.com", 587)
        a.starttls()
        a.login(mail, "vjmoezoordwzivws")
        a.sendmail(mail, self.e_ig.get(), msg)
        a.quit