import os
import sys
import random
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSharedMemory
from assistant_name import NamingPage
from speech_recognition import recognize_speech
from tts import speak_festival
from application_control import control_application
from web_search import process_command
from log_activity import log_activity  
from time_date import process_time_date
from media_control import MediaController
from personalization import update_preferences, get_suggestions
from reminder import add_reminder, save_note, get_notes, get_reminders

# Load assistant's name
NAME_FILE = "///"  # path of file which contains the name of the assistant
ICON_PATH = "///"  # path of icon ✅ Ensure correct icon path

class SmartLap(QMainWindow):
    """Main Window for Smart Lap."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart Lap")
        self.setWindowIcon(QIcon(ICON_PATH))  # ✅ Sets correct icon
        self.setGeometry(100, 100, 300, 200)

def setup_tray(app):
    """Creates a system tray icon with a 'Cut' (exit) option."""
    tray_icon = QSystemTrayIcon(QIcon(ICON_PATH), app)
    menu = QMenu()
    
    exit_action = menu.addAction("Cut")
    exit_action.triggered.connect(app.quit)  # ✅ Closes the application

    tray_icon.setContextMenu(menu)
    tray_icon.show()
    return tray_icon

def get_assistant_name():
    """Retrieves the assistant's name from a file or opens the naming page if missing."""
    if not os.path.exists(NAME_FILE):  
        app = QApplication(sys.argv)
        naming_page = NamingPage()
        naming_page.show()
        app.exec_()  # Start GUI loop to set name

    # Retrieve and return the name
    with open(NAME_FILE, "r") as f:
        return f.read().strip()

def main():
    assistant_name = get_assistant_name()

    # ✅ Check for multiple instances AFTER setting the name  
    APP_NAME = "SmartLap"
    shared_memory = QSharedMemory(APP_NAME)
    if not shared_memory.create(1):  # If memory already exists, exit
        print("Smart Lap is already running.")
        sys.exit(0)

    # ✅ Initialize GUI & system tray  
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(ICON_PATH))  # ✅ Global icon setting
    tray = setup_tray(app)

    speak_festival(f"Hello! I am {assistant_name}. How can I assist you?")
    media = MediaController()

    while True:
        command = recognize_speech().lower()

        if "exit" in command or "bye" in command or "sleep" in command or "leave" in command:
            speak_festival(f"Goodbye from {assistant_name}, call me anywhere, anytime, I will always be with you.")
            break

        elif command == assistant_name.lower():
            response = random.choice([
                "Hey! Hi, how can I help you?",
                "Hello! Do I need to open any application, play songs, or search something on Google or YouTube?",
                "Hi there! Tell me anything you want me to do. I'm always here to assist you."
            ])

        else:
            update_preferences(command)  # Track user command usage
            suggestion = get_suggestions()  # Get frequent command suggestions
            
            # Handle Reminders & Notes
            if "remind me to" in command:
                response = add_reminder(command)

            elif any(phrase in command for phrase in ["save a note", "same a note", "same a not", "save not", "same not"]):
                note = command.replace("save a note", "").strip()
                response = save_note(note)

            elif "what are my notes" in command:
                response = get_notes()

            elif "what are my reminders" in command:
                response = get_reminders()

            else:
                response = process_time_date(command) or process_command(command)

                if response == "Command not recognized.":
                    response = control_application(command)

                if any(word in command for word in ["pause", "stop", "next", "previous", "play"]):
                    response = media.control_media(command.split()[0])

                if suggestion:  # Suggest frequently used actions
                    speak_festival(suggestion)

        speak_festival(response)
        log_activity(command, response)

if __name__ == "__main__":
    main()
