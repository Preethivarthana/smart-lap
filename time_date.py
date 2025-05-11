import datetime

def get_time():
    """Returns the current time in HH:MM AM/PM format."""
    now = datetime.datetime.now()
    return now.strftime("The current time is %I:%M %p.")

def get_date():
    """Returns the current date in a readable format."""
    now = datetime.datetime.now()
    return now.strftime("Today's date is %A, %B %d, %Y.")

def process_time_date(command):
    """Processes user command to provide time or date."""
    command = command.lower()
    if "time" in command:
        return get_time()
    elif "date" in command:
        return get_date()
    else:
        return None  # Not a time/date-related command
