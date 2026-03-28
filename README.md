# 🎵 YouTube Playlist Automation (Telugu Songs)

## 📌 About This Project

This project automates the process of creating a YouTube playlist from a list of songs.

Instead of manually searching and adding each song, this tool:

* Reads song names from a file
* Searches them on YouTube
* Automatically adds them to a playlist
* Avoids duplicate songs
* Resumes from where it stopped

It is especially useful for large collections like Saregama Carvaan song lists.

---

## 🚀 Features

* 🔐 Secure login using Google OAuth
* 🎧 Automatic playlist creation
* 🔍 Smart YouTube search
* 🔁 Resume support (no need to start over)
* ❌ No duplicate songs
* ⚡ Quota-safe (handles API limits)
* 📄 Progress tracking using files

---

## 📥 How to Download & Use

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ytmusic-playlist-bot.git
cd ytmusic-playlist-bot
```

---

### 2️⃣ Install required libraries

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Setup Google API

1. Go to Google Cloud Console
2. Enable **YouTube Data API v3**
3. Create **OAuth Client ID (Desktop App)**
4. Download the file and place it in project folder as:

```text
client_secret.json
```

---

### 4️⃣ Add your songs

Edit `songs.txt` and add your song list:

```text
Ennenno Janmala Bandham Pooja
Kanne Pillavani Aakali Rajyam
Lahiri Lahiri Lo Maya Bazaar
...
```

---

### 5️⃣ Run the project

```bash
python youtube_playlist.py
```

👉 First time:

* Browser will open
* Login to your Google account
* Allow permissions

---

## 🔄 How It Works

1. Reads songs from `songs.txt`
2. Searches each song on YouTube
3. Adds to playlist
4. Saves completed songs in `done.txt`
5. Continues from next song in future runs

---

## 📂 Project Files

* `youtube_playlist.py` → Main script
* `songs.txt` → Input songs
* `done.txt` → Tracks completed songs
* `playlist_id.txt` → Stores playlist ID
* `requirements.txt` → Dependencies

---

## ⚠️ Important Notes

* API quota limit: ~100 songs per day
* Script automatically limits usage
* Do NOT upload:

  * `client_secret.json`
  * `token.pickle`

---

## 💡 Use Cases

* Create playlists from large song collections
* Convert offline lists into YouTube playlists
* Automate repetitive music tasks

---

## 🤝 Contributing

Feel free to fork the repo and improve it. Suggestions and pull requests are welcome!

---

## ⭐ Support

If you found this helpful, give this project a ⭐ on GitHub!
