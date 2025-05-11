# SMART LAP
Smart Lap is a voice-controlled assistant for Linux Mint systems. It lets you open applications, manage files, play media, search the web, and get real-time updates using just your voice. Fully system-based, it ensures data privacy without cloud services. Lightweight, fast, and secure—Smart Lap makes Linux more interactive and hands-free.

**1. Project Overview**
Description:
The Smart Lap project is a voice-controlled assistant designed for Linux systems, aiming to streamline daily tasks and enhance productivity. The assistant uses speech recognition to perform various tasks like opening files, managing applications, playing media, setting reminders, and providing real-time information like weather updates or news. Built with Python, it integrates tools like Vosk for offline speech recognition, Festival for text-to-speech, and Tkinter for the graphical interface.

Technologies Used:

Python: Core programming language.

Vosk: Offline speech recognition model.

Festival: Text-to-speech synthesis.

Tkinter: GUI for user interaction.

JSON: For handling log files and data operations.

Cron: For scheduling tasks like reminders.


**2. Features/Functionalities**
Voice Control: Control the system using voice commands (e.g., "Open YouTube", "Play music").

Speech Recognition: Utilizes Vosk for offline voice recognition.

Text-to-Speech: Reads text aloud using Festival.

Web Search: Perform web searches and open websites using voice commands.

Media Control: Play, pause, and manage media files like songs and videos.

Real-Time Reminders & Notes: Create voice-based reminders and take voice notes.

File Management: Open files and applications using voice commands.

Customizable Assistant Name: You can customize the name of the assistant.


**3 :STEP-BY-STEP INSTALLATION PROCESS**

  **1:** Create a separate folder for the Smart Lap project.
  Example: `SMART_LAP`
  
  **2:** Download the Vosk speech recognition model and place it inside the Smart Lap project folder.
  
  **3:** Create all the `.py` files on your local Linux Mint system.
  
  **4:** In the `assistant_name.py` file, paste the path of the `.txt` file to save the name of your assistant.
  Example: `/home/user1/project_folder/assistant_name.txt`
  
  **5:** In the `speechrecognition.py` file, paste the path of the Vosk model.
  
  **6:** In the `log_activity.py` file, paste the path for the log file (`*.ods` file).
  Example: `/home/user1/project_folder/log.ods`
  
  **7:** In `main.py`, paste the correct path of the assistant name file (`assistant_name.txt`) and the path of the icon image (you can use the given icon image or your own).
  
  **8:** In the `web_search.py` file, don't forget to place your favorite playlist ID.
  
  **9:** For the text-to-speech file (`tts.py`), you need to install **Festival** on your laptop via the terminal.
  
  **10:** After completing the file setup, you need to start working on the terminal and communicate with the Linux system by setting up the `.sh` file and `.desktop` file.
  
  
  
  **11:** **smart\_lap.sh**
  Create a startup script. This is important to trigger Smart Lap when the system turns on.
  
  * Run the following command in your terminal:
  
    ```
    nano <path of sh file>
    ```
  
    Example:
  
    ```
    nano /home/user1/project_folder/smart_lap.sh
    ```
  * Paste the given content into the `smart_lap.sh` file. Don't forget to update the `main.py` path.
  * After that, open the terminal and run the following command to make the `.sh` file executable:
  
    ```
    chmod +x <path of sh file>
    ```
  
    Example:
  
    ```
    chmod +x /home/user1/project_folder/smart_lap.sh
    ```
  * Save and Exit (CTRL+X, then Y, then ENTER).
  
  
  **12:** **Desktop file**
  The desktop file is used to add the Smart Lap project to the application list, which is also an important step.
  
  * Run the following command in your terminal:
  
    ```
    nano ~/.local/share/applications/smart_lap.desktop
    ```
  * Paste the given content into the `smart_lap.desktop` file. Don't forget to update all the paths.
  * After that, open the terminal and run the following command to make it executable:
  
    ```
    chmod +x ~/.local/share/applications/smart_lap.desktop
    ```
  * Save and Exit (CTRL+X, then Y, then ENTER).
  
  
  **13:** Reload the application menu by running the following command in the terminal:
  
  ```
  update-desktop-database ~/.local/share/applications/
  ```
  
  **14:** Run and test the application manually by executing the following command in the terminal:
  
  ```
  gtk-launch smart_lap
  ```
  
  **15:** Go to the **Startup Applications** menu and add the Smart Lap project.
  
  **16:** Your project is completely ready and will run when the laptop is turned on.
  
  
  
  **Note:**
  You can run the project on any IDE after completing step 9. The rest of the steps are for setting up a startup application.


**4. Usage Instructions**
Once you’ve installed Smart Lap, here’s how you can use it:

Starting the Assistant:

You can launch Smart Lap manually from the application menu or use the terminal:

gtk-launch smart_lap


Voice Commands:

To open a file or application, say:
"Open [file name]"
Example: "Open YouTube"

To play music or video, say:
"Play [song/video]"
Example: "Play my favorite song"

Set a Reminder:

Say: "Remind me to [task] at [time]"
Example: "Remind me to call John at 5 PM"

Taking Notes:

Say: "Save a note: [note]"
Example: "Save a note: Buy groceries"

Customize Assistant Name:

Edit the assistant_name.txt file to change the name of your assistant.


**5. Contributing**
We welcome contributions to improve Smart Lap! To contribute:

Fork the repository.

Create a new branch for your feature or bug fix.

Make your changes.

Push your changes and create a pull request with a description of your changes.


**6. Dependencies**
To get started with Smart Lap, make sure you have the following dependencies installed:

Vosk: For offline speech recognition.
```
pip install vosk
```

Festival: For text-to-speech synthesis.
```
sudo apt-get install festival
```

Tkinter: For GUI (Usually pre-installed with Python, but if not, you can install it with):
```
sudo apt-get install python3-tk
```

**CONCLUSION**

Congratulations! You have successfully set up Smart Lap on your Linux Mint system. This voice assistant is now ready to perform tasks such as retrieving system time, searching the web, playing media, and more, all via voice commands. With easy configuration steps and the use of powerful libraries like Vosk and Festival, Smart Lap offers a seamless experience for hands-free interaction with your computer.

Feel free to customize and extend Smart Lap to fit your personal needs. We hope this project helps you dive deeper into voice-enabled applications and provides a useful tool for your daily tasks.

If you encounter any issues or have suggestions for improvements, feel free to open an issue or contribute to the project. Enjoy using Smart Lap!
