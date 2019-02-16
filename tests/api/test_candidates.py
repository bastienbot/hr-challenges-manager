import json
import requests
import unittest


class TestApi(unittest.TestCase):

    host = 'http://localhost:5100'
    candidate = {
        "firstname": "Jean-Michel",
        "lastname": "Test",
        "email": "jean-michel.test@clevy.io",
        "phone": "0987654321"
    }
    candidate_bis = {
        "firstname": "Jean-Paul",
        "lastname": "Patest",
        "email": "jean-michel.test@clevy.io"
    }

    def test_00_create_candidate(self):
        r = requests.post(
            "{}/candidates".format(self.host),
            json=self.candidate)
        self.assertEqual(r.status_code, 200)
        res = json.loads(r.content)
        self.assertDictContainsSubset(self.candidate, res)
        self.assertIn("_id", res)
        self.assertIsNotNone(res["_id"])
        self.assertGreater(len(res["_id"]), 0)

    def test_01_get_candidate(self):
        r = requests.get(
            "{0}/candidates/{1}".format(self.host, self.candidate["email"]))
        self.assertEqual(r.status_code, 200)
        res = json.loads(r.content)
        self.assertDictContainsSubset(self.candidate, res)
        self.assertIn("_id", res)
        self.assertIsNotNone(res["_id"])
        self.assertGreater(len(res["_id"]), 0)

    def test_02_get_wrong_candidate(self):
        r = requests.get(
            "{0}/candidates/{1}err".format(self.host, self.candidate["email"]))
        self.assertEqual(r.status_code, 404)

    def test_03_put_candidate(self):
        r = requests.put(
            "{}/candidates".format(self.host),
            json=self.candidate_bis)
        self.assertEqual(r.status_code, 200)
        res = json.loads(r.content)
        self.assertDictContainsSubset(self.candidate_bis, res)
        self.assertIn("_id", res)
        self.assertIsNotNone(res["_id"])
        self.assertGreater(len(res["_id"]), 0)

    def test_04_put_wrong_candidate(self):
        wrong_candidate = self.candidate_bis
        wrong_candidate["email"] = "{}err".format(self.candidate_bis)
        r = requests.put(
            "{}/candidates".format(self.host),
            json=wrong_candidate)
        self.assertEqual(r.status_code, 404)

    def test_05_delete_candidate(self):
        r = requests.delete(
            "{0}/candidates/{1}".format(self.host, self.candidate["email"]))
        res = json.loads(r.content)
        self.assertEqual(r.status_code, 200)
        self.assertIn("aknowledged", res)
        self.assertTrue(res["aknowledged"])

    def test_05_delete_wrong_candidate(self):
        r = requests.delete(
            "{0}/candidates/{1}err".format(self.host, self.candidate["email"]))
        self.assertEqual(r.status_code, 404)

    def test_06_preview_challenge(self):
        r = requests.post(
            "{}/challenge/preview".format(self.host),
            json={"candidate": self.candidate, "job": "csm"})
        self.assertEqual(r.status_code, 200)
        # res = json.loads(r.content)
        # self.assertDictContainsSubset(self.candidate, res)
        # self.assertIn("_id", res)
        # self.assertIsNotNone(res["_id"])
        # self.assertGreater(len(res["_id"]), 0)
