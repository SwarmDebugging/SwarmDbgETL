from src.model.project import Project
import unittest
import io


class ProjectTest(unittest.TestCase):

    def test_loadProject(self):
        jsondata = '{"Task":{"Project": {"Name": "ProjectName","Description":"Desc"}}}'
        p = Project(jsondata)

        self.assertEqual(p.name, "ProjectName")
        self.assertEqual(p.description, "Desc")

    def test_loadFromFile(self):
        with io.open('../data/session.json', 'r', encoding='utf-8-sig') as file:
            jsondata = file.read()
        project = Project(jsondata)
        self.assertEqual(project.name, "Legislacao.sln")


if __name__ == '__main__':
    unittest.main()
