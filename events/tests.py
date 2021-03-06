from django.test import TestCase

class EventTestCase(TestCase):
    def test_invalid_request(self):
        response = self.client.patch("/events/", {"title": "Can't update or delete"})
        self.assertTrue(response.status_code != 200)
        response = self.client.delete('/events/')
        self.assertTrue(response.status_code != 200)
    def test_valid_request(self):
        response = self.client.get("/events/", {"title": "Should be able to get"})
        self.assertTrue(response.status_code == 200)