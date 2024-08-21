from django.test import TestCase
from django.urls import reverse
from profiles.models import Profile, User
from unittest.mock import patch


class ProfileViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.profile = Profile.objects.create(user=self.user)

    def test_all_profiles(self):
        response = self.client.get(reverse("profiles:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/index.html")

    def test_one_profile(self):
        response = self.client.get(reverse("profiles:profile", args=["testuser"]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")
        self.assertEqual(response.context["profile"], self.profile)

    def test_profiles_models(self):
        response = self.client.get(reverse("profiles:index"))
        self.assertContains(response, self.profile.user.username)

    def test_profile_view_not_found(self):
        response = self.client.get(
            reverse("profiles:profile", args=["nonexistentuser"])
        )
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")

    def test_profile_view_with_unexpected_error(self):
        with patch(
            "profiles.views.Profile.objects.get",
            side_effect=Exception("Unexpected error"),
        ):
            with self.assertLogs("django.request", level="ERROR"):
                url = reverse("profiles:profile", args=[self.user.username])
                response = self.client.get(url)
                self.assertEqual(response.status_code, 500)
                self.assertTemplateUsed(response, "500.html")

    def test_index_view_with_unexpected_error(self):
        with patch(
            "profiles.views.Profile.objects.all",
            side_effect=Exception("Unexpected error"),
        ):
            with self.assertLogs("django.request", level="ERROR"):
                url = reverse("profiles:index")
                response = self.client.get(url)

                self.assertEqual(response.status_code, 500)
                self.assertTemplateUsed(response, "500.html")
