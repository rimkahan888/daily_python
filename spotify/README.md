


          
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


        
