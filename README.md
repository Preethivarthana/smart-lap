# SMART LAP
Smart Lap is a voice-controlled assistant for Linux Mint systems. It lets you open applications, manage files, play media, search the web, and get real-time updates using just your voice. Fully system-based, it ensures data privacy without cloud services. Lightweight, fast, and secure—Smart Lap makes Linux more interactive and hands-free.




**STEP-BY-STEP INSTALLATION PROCESS**

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


