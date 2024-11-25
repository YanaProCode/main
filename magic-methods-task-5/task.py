import os
import shutil
import uuid

class TempDir:

    # TODO: please ad your code here
    def __enter__(self):
        self.current_path = os.getcwd() #getting current working directory
        filename = uuid.uuid4().hex
        self.new_file = os.path.join(self.current_path, filename)
        os.mkdir(self.new_file)
        os.chdir(self.new_file)
        return self.new_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.current_path)
        shutil.rmtree(self.new_file)

