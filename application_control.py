import subprocess

# Function to open applications
def open_application(command):
    app = None
    if "text editor" in command:
        app = "xed"  # Default text editor for Linux Mint
    elif "files" in command:
        app = "nemo"  # Default file manager for Linux Mint
    elif "browser" in command:
        app = "firefox"  # Default web browser
    elif "terminal" in command:
        app = "gnome-terminal"  # GNOME terminal
    elif "calculator" in command:
        app = "gnome-calculator"  # GNOME calculator
    elif "settings" in command:
        app = "cinnamon-settings"  # cinnamon-settings
    elif "code" in command or "vs code" in command:
        app = "code"  # Visual Studio Code
    elif "writer" in command:
        app = "libreoffice --writer"  # LibreOffice Writer
    elif "excel" in command:
        app = "libreoffice --calc"  # LibreOffice Calc
    elif "ppt" in command:
        app = "libreoffice --impress"  # LibreOffice Impress
    elif "notes" in command:
        app = "xpad"  # Simple sticky notes app
    elif "spotify" in command:
        app = "spotify"  # Spotify app
    else:
        return "Application not recognized for opening."

    subprocess.Popen(app, shell=True)  # Run application in background
    return f"{app.split()[0]} opened."

# Function to close applications
def close_application(command):
    app = None
    if "text editor" in command:
        app = "xed"
    elif "files" in command:
        app = "nemo"
    elif "browser" in command:
        app = "firefox"
    elif "terminal" in command:
        app = "gnome-terminal"
    elif "calculator" in command:
        app = "gnome-calculator"
    elif "settings" in command:
        app = "cinnamon-settings"
    elif "code" in command or "vs code" in command:
        app = "code"
    elif "writer" in command:
        app = "libreoffice --writer"
    elif "excel" in command:
        app = "libreoffice --calc"
    elif "ppt" in command:
        app = "libreoffice --impress"
    elif "notes" in command:
        app = "xpad"
    elif "spotify" in command:
        app = "spotify"
    else:
        return "Application not recognized for closing."

    subprocess.run(f"pkill -f {app.split()[0]}", shell=True, executable='/bin/bash')
    return f"{app.split()[0]} closed."



# Central function to decide open or close
def control_application(command):
    if "open " in command:
        return open_application(command)
    elif "close " in command:
        return close_application(command)
    else:
        return "Command not understood."
