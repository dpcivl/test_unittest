import time
import random

class RandomDelayService:
    def __init__(self, min_delay=1, max_delay=5):
        self.min_delay = min_delay
        self.max_delay = max_delay

    def call_service(self):
        delay = random.uniform(self.min_delay, self.max_delay)
        print(f"Delaying for {delay:.2f} seconds...")
        time.sleep(delay)  # 실제 지연 발생
        return "Service called after delay"
