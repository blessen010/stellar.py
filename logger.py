import json
import os

LOG_FILE_PATH = './message_logs.json'

# Ensure the log file exists and is a list
def initialize_log_file():
    if not os.path.exists(LOG_FILE_PATH):
        with open(LOG_FILE_PATH, 'w') as f:
            json.dump([], f)
    else:
        with open(LOG_FILE_PATH, 'r') as f:
            try:
                data = json.load(f)
                if not isinstance(data, list):
                    raise ValueError("Log file is not a list")
            except (json.JSONDecodeError, ValueError):
                with open(LOG_FILE_PATH, 'w') as f:
                    json.dump([], f)

# Function to log messages
def log_message(username, message, time):
    with open(LOG_FILE_PATH, 'r') as f:
        try:
            logs = json.load(f)
        except json.JSONDecodeError:
            logs = []

    logs.append({
        'username': username,
        'message': message,
        'time': time
    })

    with open(LOG_FILE_PATH, 'w') as f:
        json.dump(logs, f, indent=4)
