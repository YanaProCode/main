from contextlib import ContextDecorator
import datetime
import traceback


class LogFile(ContextDecorator):
    def __init__(self, file):
        self.file = file

    def __enter__(self):
        self.start_time = datetime.datetime.now()
        with open(self.file, "a") as f:
            f.write("Start: {} | ".format(self.start_time))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = datetime.datetime.now()
        self.run_time = self.end_time - self.start_time
        with open(self.file, "a") as f:
            f.write(f"Run: {self.run_time} | An error occurred: {exc_val}\n")
        return False



