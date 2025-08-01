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
    
    
