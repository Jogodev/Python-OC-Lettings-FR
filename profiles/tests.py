from django.test import TestCase
from django.urls import reverse
from profiles.models import Profile, User


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
