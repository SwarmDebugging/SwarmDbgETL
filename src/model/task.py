import json


class Task:
    TASK_FIELD = 'Task'
    NAME_FIELD = 'Name'
    DESCRIPTION_FIELD = 'Description'
    ACTION_FIELD = 'Action'
    CREATED_FIELD = 'Created'

    def __init__(self, jsondata):
        self.name = ''
        self.description = ''
        self.action = ''
        self.created = None
        self.load(jsondata)

    def load(self, jsondata):
        data = json.loads(jsondata)
        self.name = data[Task.TASK_FIELD][Task.NAME_FIELD]
        self.description = data[Task.TASK_FIELD][Task.DESCRIPTION_FIELD]
        self.action = data[Task.TASK_FIELD][Task.ACTION_FIELD]
        self.created = data[Task.TASK_FIELD][Task.CREATED_FIELD]

