from src.model.task import Task
import unittest
import io


class TaskTest(unittest.TestCase):

    def test_loadTask(self):
        jsondata = '{"Task":{"Name": "TaskName","Description":"Desc",  \
                   "Action":"MyAction", "Created":"2017-11-27T17:02:37.2212804-02:00"}}'
        task = Task(jsondata)

        self.assertEqual(task.name, "TaskName")
        self.assertEqual(task.description, "Desc")
        self.assertEqual(task.action, "MyAction")
        self.assertEqual(task.created, "2017-11-27T17:02:37.2212804-02:00")

    def test_loadFromFile(self):
        with io.open('../data/session.json', 'r', encoding='utf-8-sig') as file:
            jsondata = file.read()
        task = Task(jsondata)
        self.assertEqual(task.name, "SmtpTest")


if __name__ == '__main__':
    unittest.main()
