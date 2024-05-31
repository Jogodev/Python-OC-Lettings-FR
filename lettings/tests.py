from django.test import TestCase
from django.urls import reverse
from lettings.models import Letting, Address


class LettingsTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=20,
            street="Test Street",
            city="Test City",
            state="TS",
            zip_code=12345,
            country_iso_code="TST",
        )
        self.letting1 = Letting.objects.create(title="Letting 1", address=self.address)

    def test_all_lettings(self):
        response = self.client.get(reverse("lettings:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/index.html")
        self.assertContains(response, self.letting1.title)
        self.assertContains(response, self.address.number)

    def test_one_letting(self):
        letting = Letting.objects.get(title="Letting 1")
        response = self.client.get(reverse("lettings:letting", args=[letting.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/letting.html")
        self.assertContains(response, letting.title)

    def test_letting_not_found(self):
        response = self.client.get(reverse("lettings:letting", args=[999]))
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")
