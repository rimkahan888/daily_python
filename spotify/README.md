


          
Here's a comprehensive README.md file for your Spotify Album Track Counter project:

```markdown:/Users/johankarim/Desktop/coding_project/python.daily/python.1/README.md
# Spotify Album Track Counter

A Python application that uses the Spotify Web API to retrieve and analyze album information, including track counts and detailed track listings.

## 🎵 Features

- **Album Track Counting**: Get the total number of tracks in any Spotify album
- **Detailed Track Information**: View complete track listings with duration
- **Interactive Menu**: User-friendly command-line interface
- **Example Albums**: Pre-loaded with popular albums for quick testing
- **Custom Album Support**: Enter any Spotify album ID for analysis
- **Error Handling**: Robust error handling for API issues and invalid inputs

## 📋 Prerequisites

- Python 3.6 or higher
- Spotify Developer Account
- Internet connection for API calls

## 🔧 Installation

1. **Clone or download this repository**

2. **Install required dependencies:**
   ```bash
   pip install requests
   ```

3. **Set up Spotify API credentials:**
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications)
   - Create a new app
   - Copy your Client ID and Client Secret
   - Replace the placeholder values in the script:
     ```python
     CLIENT_ID = "your_actual_client_id_here"
     CLIENT_SECRET = "your_actual_client_secret_here"
     ```

      ## 🚀 Usage

### Running the Application

```bash
python spotify_album_tracks.py
```

### Menu Options

1. **Enter Custom Album ID**
   - Input any Spotify album ID to analyze
   - Album IDs can be found in Spotify URLs (e.g., `4LH4d3cOWNNsVw41Gqt2kv`)

2. **Try Example Albums**
   - Choose from pre-loaded popular albums:
     - Abbey Road - The Beatles
     - Thriller - Michael Jackson
     - The Dark Side of the Moon - Pink Floyd

3. **Exit**
   - Close the application

### Sample Output

```
📀 Album: Abbey Road
🎵 Artist(s): The Beatles
📊 Total tracks: 17

📝 Track List:
   1. Come Together (4:19)
   2. Something (3:03)
   3. Maxwell's Silver Hammer (3:27)
   ...

🎯 Result: This album contains 17 tracks
```

## 🔍 How to Find Album IDs

1. **From Spotify Web Player:**
   - Open an album in Spotify web player
   - Copy the album ID from the URL: `https://open.spotify.com/album/[ALBUM_ID]`

2. **From Spotify Desktop App:**
   - Right-click on an album → Share → Copy Spotify URI
   - Extract the ID from: `spotify:album:[ALBUM_ID]`

## 📁 Project Structure

```
spotify_album_tracks.py
├── SpotifyAlbumTracker class
│   ├── __init__()           # Initialize with credentials
│   ├── get_access_token()   # Authenticate with Spotify API
│   └── get_album_tracks_count() # Fetch and analyze album data
└── main()                   # Interactive command-line interface
```

## 🔐 Authentication

This application uses Spotify's **Client Credentials** flow:
- Suitable for server-to-server authentication
- No user login required
- Access to public album data only
- Tokens are automatically managed

## 🛠️ API Endpoints Used

- **Token Endpoint**: `https://accounts.spotify.com/api/token`
- **Albums Endpoint**: `https://api.spotify.com/v1/albums/{id}`

## ⚠️ Error Handling

The application handles various error scenarios:

- **Invalid Credentials**: Check your Client ID and Client Secret
- **Album Not Found (404)**: Verify the album ID is correct
- **Network Issues**: Check your internet connection
- **Rate Limiting**: Automatic handling of API rate limits
- **Invalid Input**: User-friendly error messages for invalid selections

## 🔒 Security Notes

- Never commit your actual Client ID and Client Secret to version control
- Consider using environment variables for credentials:
  ```python
  import os
  CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
  CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
  ```

## 📝 Example Albums Included

| Album | Artist | Spotify ID |
|-------|--------|------------|
| Abbey Road | The Beatles | `0ETFjACtuP2ADo6LFhL6HN` |
| Thriller | Michael Jackson | `2ANVost0y2y52ema1E9xAZ` |
| The Dark Side of the Moon | Pink Floyd | `4LH4d3cOWNNsVw41Gqt2kv` |

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).


