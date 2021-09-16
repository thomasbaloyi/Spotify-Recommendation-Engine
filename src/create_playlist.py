import requests

user_id = ""
create_playlist_url = f"https://api.spotify.com/v1/users/{user_iD}/playlists"
access_token = "1BQBaJ1k5Pa2WA9PNkyNc2Bmtkum0cPSR06xgYi5doQBzs8Ouo5RVHfktQ5fNT0dhq4xY46ONEkbeYlPAULUReupZCqaPabbUIRZRkNVkvysZyjKzrcWzX_dheYzEr8AAUJhUOYcS1TNp0jIm8Afq1sKbQPKajgCI4Uvye51XziqCEm2e1aybaTKd6xm2aJ_3cgZOHIG6QX_4"

def createPlaylist(name, description, public):
    response = requests.post(
        create_playlist_url,
        headers={
            "Authorization": f"Bearer {access_token}"
        },
        json={
            "name": name,
            "description": description,
            "public": public
        }
    )

    json_resp = response.json()
    return json_resp

def main():
    playlist = createPlaylist(
        name = "A private playlist",
        description = "A bunch of random songs",
        public = False
    )

    print(f"Playlist: {playlist}")

if __name__ == '__main__':
    main()