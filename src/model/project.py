import json
from src.model.task import Task


class Project:
    PROJECT_FIELD = 'Project'
    NAME_FIELD = 'Name'
    DESCRIPTION_FIELD = 'Description'

    def __init__(self, jsondata):
        self.name = ''
        self.description = ''
        self.load(jsondata)

    def load(self, jsondata):
        data = json.loads(jsondata)
        self.name = data[Task.TASK_FIELD][Project.PROJECT_FIELD][Project.NAME_FIELD]
        self.description = data[Task.TASK_FIELD][Project.PROJECT_FIELD][Project.DESCRIPTION_FIELD]
