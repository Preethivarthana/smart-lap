import os
import subprocess
import time

class MediaController:
    def __init__(self):
        self.media_players = ["spotify", "vlc"]
    
    def get_active_player(self):
        """Check for an active media player."""
        try:
            result = subprocess.check_output(["playerctl", "-l"], stderr=subprocess.DEVNULL).decode().strip()
            active_players = result.split("\n")
            for player in self.media_players:
                if player in active_players:
                    return player
            return None
        except subprocess.CalledProcessError:
            return None

    def control_media(self, action):
        """Execute media control commands."""
        player = self.get_active_player()
        if not player:
            return "No active media player found."
        
        if action in ["play", "pause", "stop", "next", "previous"]:
            try:
                subprocess.run(["playerctl", "-p", player, action], check=True)
                return f"Executed {action} on {player}"
            except subprocess.CalledProcessError:
                return f"Failed to execute {action} on {player}"
        else:
            return "Invalid media control command."
        