from src.model.developer import Developer
import unittest
import io


class DeveloperTest(unittest.TestCase):

    def test_loadDeveloper(self):
        jsondata = '{"Developer": {"Name": "John"}}'
        developer = Developer(jsondata)

        self.assertEqual(developer.name, "John")

    def test_loadFromFile(self):
        with io.open('../data/session.json', 'r', encoding='utf-8-sig') as file:
            jsondata = file.read()

        developer = Developer(jsondata)

        self.assertEqual(developer.name, "SEFAZRS\\Dev.AbelL")


if __name__ == '__main__':
    unittest.main()
