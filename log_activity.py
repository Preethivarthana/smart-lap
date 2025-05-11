import os
import datetime
import pyexcel_ods3

def log_activity(command, action):
    """Logs command and action performed in a LibreOffice Calc file (log.ods)."""
    log_file = "/home/preethi/SMART_LAP/log.ods"
    sheet_name = "Activity Log"
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Check if log file exists, else create a new one with headers
    if not os.path.exists(log_file):
        data = {sheet_name: [["Timestamp", "Command Received", "Action Performed"]]}
        pyexcel_ods3.save_data(log_file, data)
    
    # Load existing data and append the new log
    data = pyexcel_ods3.get_data(log_file)
    if sheet_name not in data:
        data[sheet_name] = [["Timestamp", "Command Received", "Action Performed"]]
    
    data[sheet_name].append([timestamp, command, action])
    pyexcel_ods3.save_data(log_file, data)
    
    print(f"Logged: {timestamp} | Command: {command} | Action: {action}")
