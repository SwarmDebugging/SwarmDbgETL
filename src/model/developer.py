import json


class Developer:
    DEVELOPER_FIELD = 'Developer'
    NAME_FIELD = 'Name'

    def __init__(self, jsondata):
        self.name = ''
        self.load(jsondata)

    def load(self, jsondata):
        data = json.loads(jsondata)
        self.name = data[Developer.DEVELOPER_FIELD][Developer.NAME_FIELD]
