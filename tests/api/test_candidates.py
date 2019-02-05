import json
import requests
import unittest


class TestApi(unittest.TestCase):

    host = 'http://localhost:5100'
    candidate = {
        "firstname": "Jean-Michel",
        "lastname": "Test",
        "email": "jean-michel.test@clevy.io"
    }

    def test_00_create_candidate(self):
        r = requests.post(
            "{}/candidates".format(self.host),
            json=self.candidate)
        self.assertEqual(r.status_code, 200)
        res = json.loads(r.content)
        self.assertDictContainsSubset(self.candidate, res)
        self.assertIn("id", res)
        self.assertIsNotNone(res["id"])
        self.assertGreater(len(res["id"]), 0)
