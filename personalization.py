import json
import os

PREFERENCES_FILE = "preferences.json"

def load_preferences():
    """Load user preferences from a JSON file."""
    if os.path.exists(PREFERENCES_FILE):
        with open(PREFERENCES_FILE, "r") as file:
            return json.load(file)
    return {}

def save_preferences(preferences):
    """Save updated preferences to the JSON file."""
    with open(PREFERENCES_FILE, "w") as file:
        json.dump(preferences, file, indent=4)

def update_preferences(command):
    """Track frequently used commands and store them."""
    preferences = load_preferences()

    if command in preferences:
        preferences[command] += 1  # Increment frequency count
    else:
        preferences[command] = 1  # First-time command usage

    save_preferences(preferences)

def get_suggestions():
    """Suggest frequently used actions."""
    preferences = load_preferences()

    if not preferences:
        return None  # No suggestions if no history exists

    # Find the most frequently used command
    frequent_command = max(preferences, key=preferences.get)
 

    if preferences[frequent_command] > 3:  # Suggest if used more than 3 times
        return f"Would you like to repeat '{frequent_command}'?"
    
    return None


