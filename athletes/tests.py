from django.test import TestCase

class AthleteTestCase(TestCase):
    def test_invalid_request(self):
        response = self.client.patch("/athletes/", {"title": "Can't update or delete"})
        self.assertTrue(response.status_code != 200)
        response = self.client.delete('athletes/')
        self.assertTrue(response.status_code != 200)
    def test_valid_request(self):
        response = self.client.get("/athletes/", {"title": "Should be able to get"})
        self.assertTrue(response.status_code == 200)