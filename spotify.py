import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

class SpotifyAddMusic:
    def __init__(self, client_id, client_secret, date):
        self.REDIRECT_URI = "http://example.com" 
        self.CLIENT_ID = client_id
        self.CLIENT_SECRECT = client_secret
        self.date = date
        
    def run(self):
        sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope="playlist-modify-private",
                redirect_uri=self.REDIRECT_URI,
                client_id= self.CLIENT_ID,
                client_secret=self.CLIENT_SECRECT,
                show_dialog= True,
                cache_path="token.json",
                )
            )


        user_id = sp.current_user()['id']
        print("User ID => ", user_id)

        billboard_endpoint_url = f"https://www.billboard.com/charts/hot-100/{self.date}"
        response = requests.get(billboard_endpoint_url)
        billboard_website = response.text
        print("Response status => ", response.status_code)
        soup = BeautifulSoup(billboard_website, "html.parser")
        print("Response text => ", soup.prettify())

        albums_title = soup.select(selector= "li .c-title")
        song_names = [item.getText().strip("\n\t") for item in albums_title]
        print("SONG NAMES => ", song_names)

        song_uris = []
        print('song_uris => ', song_uris)
        year = self.date.split("-")[0]

        for song in song_names:
            result = sp.search(q=f"track:{song} year:{year}", type="track")
            try:
                uri = result["tracks"]["items"][0]["uri"]
                song_uris.append(uri)
            except IndexError:
                print(f"\n{song} doesn't exist in Spotify. Skipped.\n")

        playlist = sp.user_playlist_create(
            user= user_id,
            name= f"{year} Billboard 100",
            public= False
        )
        # print(playlist)
        sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
