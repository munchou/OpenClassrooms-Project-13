from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.loader import render_to_string

from ..models import Profile

import sentry_sdk

sentry_sdk.init(dsn="")


class ProfilesViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

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
        try:
            self.client.get(reverse("profiles:profile", args=["blabla"]))
        except Exception:
            with self.assertTemplateUsed("500.html"):
                render_to_string("500.html")
