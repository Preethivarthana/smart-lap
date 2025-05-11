import json
import os
import datetime
import subprocess
import dateparser
from word2number import w2n
import re

REMINDER_FILE = "reminders.json"

def load_reminders():
    """Load reminders and notes from a JSON file."""
    if os.path.exists(REMINDER_FILE):
        with open(REMINDER_FILE, "r") as file:
            return json.load(file)
    return {"reminders": [], "notes": []}

def save_reminders(data):
    """Save reminders and notes to the JSON file."""
    with open(REMINDER_FILE, "w") as file:
        json.dump(data, file, indent=4)

def convert_text_to_numbers(text):
    """Converts spoken numbers into numerical format (e.g., 'five PM' → '5 PM')."""
    
    words = text.lower().split()  # Convert to lowercase for consistency
    converted_words = []

    for word in words:
        try:
            converted_word = str(w2n.word_to_num(word))  # Convert word numbers
        except ValueError:
            converted_word = word  # Keep original word if not a number

        converted_words.append(converted_word)

    # Convert "p m" or "a m" into "PM" or "AM"
    converted_text = " ".join(converted_words)
    converted_text = re.sub(r"\b(p m|pm)\b", "PM", converted_text)
    converted_text = re.sub(r"\b(a m|am)\b", "AM", converted_text)

    return converted_text

def extract_time_from_text(text):
    """Extracts the reminder message and the time-related words separately."""
    time_keywords = ["AM", "PM", "hours", "hour", "minutes", "tomorrow", "today", "at", "in", "after", "next"]
    
    words = text.split()
    time_part = []
    message_part = []
    last_was_digit = False  # Track if last word was a digit (e.g., "10 AM")

    for word in words:
        if word.isdigit():  # If it's a number, treat it as part of time
            time_part.append(word)
            last_was_digit = True
        elif any(keyword in word.lower() for keyword in time_keywords):
            time_part.append(word)
            last_was_digit = False
        elif last_was_digit:  # Handle cases like "10 AM"
            time_part.append(word)
            last_was_digit = False
        else:
            message_part.append(word)

    return " ".join(message_part), " ".join(time_part)


def add_reminder(command):
    """Adds a reminder with automatic time extraction and scheduling."""
    data = load_reminders()

    # Extract message and time separately
    message, time_text = extract_time_from_text(command)

    if not time_text:
        return "I couldn't understand the reminder time. Try including a valid time."

    # Convert spoken words to numbers
    time_text = convert_text_to_numbers(time_text)

    # Ensure "after/in" phrases are correctly parsed by dateparser
    if "after" in time_text or "in" in time_text:
        time_text = "in " + time_text  # Ensures dateparser correctly interprets relative times

    # Convert natural language time to a datetime object
    reminder_time = dateparser.parse(time_text)
    
    if not reminder_time:
        return f"I couldn't understand the reminder time: {time_text}. Try saying it more clearly."

    if reminder_time < datetime.datetime.now():
        return "This time has already passed. Please specify a future time."

    pre_alert = 10  # Default pre-alert time
    pre_reminder_time = reminder_time - datetime.timedelta(minutes=pre_alert)

    data["reminders"].append({"message": message, "time": reminder_time.strftime("%Y-%m-%d %H:%M:%S")})
    save_reminders(data)

    # Schedule Pre-Reminder with cron
    pre_cron_time = pre_reminder_time.strftime("%M %H %d %m *")
    pre_cron_command = f'(crontab -l; echo "{pre_cron_time} DISPLAY=:0 notify-send \\"Upcoming Reminder\\" \\"{message} in {pre_alert} minutes\\"") | crontab -'
    subprocess.run(pre_cron_command, shell=True)

    # Schedule Main Reminder with cron
    event_cron_time = reminder_time.strftime("%M %H %d %m *")
    event_cron_command = f'(crontab -l; echo "{event_cron_time} DISPLAY=:0 notify-send \\"Reminder\\" \\"{message}\\"") | crontab -'
    subprocess.run(event_cron_command, shell=True)

    return f"Reminder set: '{message}' at {reminder_time.strftime('%Y-%m-%d %H:%M:%S')}. You'll also be reminded {pre_alert} minutes before."

def save_note(note):
    """Saves a note."""
    data = load_reminders()
    data["notes"].append(note)
    save_reminders(data)
    return "Note saved successfully."

def get_notes():
    """Retrieves all saved notes."""
    data = load_reminders()
    if data["notes"]:
        return "\n".join(data["notes"])
    return "No notes found."

def get_reminders():
    """Retrieves all upcoming reminders."""
    data = load_reminders()
    if data["reminders"]:
        return "\n".join([f"{r['time']} - {r['message']}" for r in data["reminders"]])
    return "No reminders found."


