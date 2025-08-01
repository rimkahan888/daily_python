import requests
import json
from typing import Optional

class SpotifyAlbumTracker:
    def __init__(self, client_id: str, client_secret: str):
        """
        Initialize the Spotify API client
        
        Args:
            client_id: Your Spotify app client ID
            client_secret: Your Spotify app client secret
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None
        self.base_url = "https://api.spotify.com/v1"
    
    def get_access_token(self) -> bool:
        """
        Get access token using Client Credentials flow
        
        Returns:
            bool: True if token obtained successfully, False otherwise
        """
        auth_url = "https://accounts.spotify.com/api/token"
        
        auth_headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        
        auth_data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        
        try:
            response = requests.post(auth_url, headers=auth_headers, data=auth_data)
            response.raise_for_status()
            
            token_data = response.json()
            self.access_token = token_data.get("access_token")
            
            if self.access_token:
                print("✅ Successfully obtained access token")
                return True
            else:
                print("❌ Failed to obtain access token")
                return False
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Error getting access token: {e}")
            return False
    
    def get_album_tracks_count(self, album_id: str) -> Optional[int]:
        """
        Get the number of tracks in a Spotify album
        
        Args:
            album_id: The Spotify album ID
            
        Returns:
            int: Number of tracks in the album, or None if error
        """
        if not self.access_token:
            print("❌ No access token available. Please authenticate first.")
            return None
        
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        
        album_url = f"{self.base_url}/albums/{album_id}"
        
        try:
            response = requests.get(album_url, headers=headers)
            response.raise_for_status()
            
            album_data = response.json()
            
            # Extract album information
            album_name = album_data.get("name", "Unknown Album")
            artist_names = [artist["name"] for artist in album_data.get("artists", [])]
            tracks = album_data.get("tracks", {}).get("items", [])
            track_count = len(tracks)
            
            # Display results
            print(f"\n📀 Album: {album_name}")
            print(f"🎵 Artist(s): {', '.join(artist_names)}")
            print(f"📊 Total tracks: {track_count}")
            
            # Optional: Display track list
            if tracks:
                print("\n📝 Track List:")
                for i, track in enumerate(tracks, 1):
                    track_name = track.get("name", "Unknown Track")
                    duration_ms = track.get("duration_ms", 0)
                    duration_min = duration_ms // 60000
                    duration_sec = (duration_ms % 60000) // 1000
                    print(f"  {i:2d}. {track_name} ({duration_min}:{duration_sec:02d})")
            
            return track_count
            
        except requests.exceptions.HTTPError as e:
            if response.status_code == 404:
                print(f"❌ Album not found. Please check the album ID: {album_id}")
            elif response.status_code == 401:
                print("❌ Unauthorized. Please check your credentials.")
            else:
                print(f"❌ HTTP Error: {e}")
            return None
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Request Error: {e}")
            return None
            
        except json.JSONDecodeError as e:
            print(f"❌ JSON Decode Error: {e}")
            return None


