from django.test import TestCase
from django.urls import reverse


class IndexViewTest(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse("home:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")
