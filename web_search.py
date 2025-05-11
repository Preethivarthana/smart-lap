import os
import time
import webbrowser
import shutil

def search_google(query):
    """Searches a query on Google."""
    url = f'https://www.google.com/search?q={query.replace(" ", "+")}'
    os.system(f'xdg-open "{url}"')
    return f"Searching for '{query}' on Google."

def play_youtube(video_name):
    """Searches and optionally plays the first video on YouTube."""
    
    # Open YouTube search results in the browser
    search_url = f"https://www.youtube.com/results?search_query={video_name.replace(' ', '+')}"
    webbrowser.open(search_url)

    # Check if yt-dlp is installed before attempting to use it
    if shutil.which("yt-dlp"):
        command = f'yt-dlp -g "ytsearch1:{video_name}" | xargs -I {{}} vlc {{}} &'
        exit_code = os.system(command)

        if exit_code == 0:
            return f"Playing '{video_name}' on YouTube."
        else:
            return f"Showing search results for '{video_name}' on YouTube."
    
    return f"Showing search results for '{video_name}' on YouTube. (yt-dlp not installed)"



def play_spotify(song_name=None):
    """Plays a song on Spotify. If no song is specified, plays a random song from a playlist."""
    
    # Ensure Spotify is running
    os.system("spotify &")
    time.sleep(5)  # Allow Spotify to load
    
    if song_name:
        # Search for a song
        os.system(f'spotify --uri "spotify:search:{song_name}"')
        time.sleep(3)  # Wait for search results
        
        # Play the first song from the search results
        os.system("playerctl next")  # Skip to the first song in the search results
        time.sleep(1)
        os.system("playerctl play")  # Ensure the song starts playing
        
        return f"Playing '{song_name}' on Spotify."
    
    else:
        # Play a specific playlist (Replace 'YOUR_PLAYLIST_ID' with actual ID)
        playlist_uri = "spotify:playlist:https://open.spotify.com/playlist/37i9dQZF1EIUtYhOXKqLCG?si=0d5e9569f2834c4e"
        os.system(f'spotify --uri "{playlist_uri}"')
        time.sleep(3)
        os.system("playerctl play")
        return "Playing a random song from your playlist."


def play_media(file_path):
    """Plays a media file using the default media player."""
    if os.path.isfile(file_path):
        os.system(f'xdg-open "{file_path}"')
        return f"Playing {file_path}"
    return f"File '{file_path}' not found."

def process_command(command):
    """Recognizes the command and executes the respective action."""
    command = command.lower()
    if "search" in command and "google" in command or ("google" in command):
        query = command.replace("search", "").replace("on google", "").strip()
        return search_google(query)
    elif ("search" in command or "find" in command or "play" in command) and "youtube" in command:
        query = command.replace("search", "").replace("find", "").replace("play", "").replace("on youtube", "").strip()
        return play_youtube(query)
    elif "play" in command and ("spotify" in command or "music" in command or "song" in command):
        query = command.replace("play", "").replace("on spotify", "").replace("music", "").strip()
        return play_spotify(query)
    elif "play song" in command:
        return play_spotify()
    else:
        return "Command not recognized."