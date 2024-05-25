from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
from oc_lettings_site.views import custom_500_view
from django.http import HttpRequest

def test_dummy():
    assert 1

class TestCustomErrorViews(TestCase):

    def test_404(self):
        response = self.client.get('prof')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response,'404.html')

    def test_500(self):
        request = HttpRequest()
        response = custom_500_view(request)
        self.assertEqual(response.status_code, 500)

