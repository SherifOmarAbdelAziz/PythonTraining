
from datetime import datetime

class Logger:

    def __init__(self, log_file):
        self.log_file = log_file

    def info(self, msg):
        timestamp = datetime.now()

        # context manager
        with open (self.log_file, "a") as f:
            f.write(f"{timestamp} [INFO] {msg}\n")

        print(f"{timestamp} [INFO] {msg}")
    
    def warning(self, msg):
        timestamp = datetime.now()

        with open (self.log_file, "a") as f:
            f.write(f"{timestamp} [WARNING] {msg}\n")

        print(f"{timestamp} [WARNING] {msg}")
    
    def error(self, msg):
        timestamp = datetime.now()

        with open (self.log_file, "a") as f:
            f.write(f"{timestamp} [ERROR] {msg}\n")

        print(f"{timestamp} [ERROR] {msg}")