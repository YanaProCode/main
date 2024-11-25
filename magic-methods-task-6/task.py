import os


class Cd:

    # TODO: please add your code here
    def __init__(self, path):
        self.path = path
        if not os.path.isdir(self.path):
            raise ValueError("Provided value is not a directory.")


    def __enter__(self):
        self.previous_dir = os.getcwd()
        os.chdir(self.path)
        return self.path

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.previous_dir)


