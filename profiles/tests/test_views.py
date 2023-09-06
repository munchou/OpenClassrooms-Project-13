from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from ..models import Profile


class ProfilesViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testouilleur", password="test1234"
        )
        self.profile = Profile.objects.create(
            user=self.user, favorite_city="Zbeurg-en-Broute"
        )

    def test_profiles_index(self):
        response = self.client.get(reverse("profiles:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/index.html")
        self.assertContains(response, "testouilleur")

    def test_profiles_profile(self):
        response = self.client.get(reverse("profiles:profile", args=["testouilleur"]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")
        self.assertContains(response, "testouilleur")
        self.assertContains(response, "Zbeurg-en-Broute")

    def test_profile_error500(self):
        response = self.client.get(reverse("profiles:profile", args=[456452312]))
        self.assertTemplateUsed(response, "500.html")
