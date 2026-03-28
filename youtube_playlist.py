import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

SCOPES = ["https://www.googleapis.com/auth/youtube"]

# ---------- AUTH ----------
def authenticate_youtube():
    creds = None

    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "client_secret.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    return build("youtube", "v3", credentials=creds)


# ---------- CREATE PLAYLIST ----------
def create_playlist(youtube, title):
    request = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": "Auto created playlist"
            },
            "status": {
                "privacyStatus": "private"
            }
        }
    )
    response = request.execute()
    return response["id"]


# ---------- SEARCH VIDEO ----------
def search_video(youtube, query):
    request = youtube.search().list(
        part="snippet",
        maxResults=1,
        q=query + " Telugu movie song original",
        type="video"
    )
    response = request.execute()

    if response["items"]:
        return response["items"][0]["id"]["videoId"]
    return None


# ---------- ADD TO PLAYLIST ----------
def add_to_playlist(youtube, playlist_id, video_id):
    youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": playlist_id,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": video_id
                }
            }
        }
    ).execute()


# ---------- MAIN ----------
def main():
    youtube = authenticate_youtube()

    playlist_id = create_playlist(youtube, "Carvaan Telugu Songs")
    print("Playlist created:", playlist_id)

    DONE_FILE = "done.txt"
    MAX_PER_RUN = 80   # avoid quota limit

    # Load completed songs
    if os.path.exists(DONE_FILE):
        with open(DONE_FILE) as f:
            done = set(line.strip() for line in f)
    else:
        done = set()

    count = 0

    with open("songs.txt") as f:
        songs = f.readlines()

    for song in songs:
        song = song.strip()

        if not song or song in done:
            continue

        if count >= MAX_PER_RUN:
            print("Reached daily limit. Run again tomorrow 👍")
            break

        print("Searching:", song)

        try:
            video_id = search_video(youtube, song)

            if video_id:
                add_to_playlist(youtube, playlist_id, video_id)
                print("Added:", song)

                # Save progress
                with open(DONE_FILE, "a") as f:
                    f.write(song + "\n")

                done.add(song)
                count += 1
            else:
                print("Not found:", song)

        except Exception as e:
            print("Error with:", song, "|", e)
            break


if __name__ == "__main__":
    main()