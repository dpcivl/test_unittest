from datetime import datetime, timedelta

class Timer:
    def __init__(self):
        self.start_time = datetime.now()

    def check_alarm(self):
        current_time = datetime.now()
        elapsed_time = current_time - self.start_time
        if elapsed_time >= timedelta(seconds=10):
            return "Alarm!"
        return "No alarm yet."
