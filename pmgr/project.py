from pathlib import Path
import os

class TaskException(Exception):
    pass

class Project(object):
    def __init__(self, name):
        self.name = name
        
        projdir = Path.cwd() / '.projects'
        if not projdir.exists():
            projdir.mkdir()

        self.filepath =  projdir / (self.name + '.txt')
        if not self.filepath.exists():
            self.filepath.touch()
        

    def add_task(self, task_name):
        pass

    def remove_task(self, task_name):
        pass

    def get_tasks(self):
        pass

