from django.test import TestCase
from django.contrib.auth.models import User

from ..models import Profile


class ProfileModelsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testouilleur", password="test1234"
        )
        self.profile = Profile.objects.create(
            user=self.user, favorite_city="Zbeurg-en-Broute"
        )

    def test_profile_fields(self):
        profile = Profile.objects.get(id=1)
        prof_fav_city = profile.favorite_city
        self.assertEqual(str(profile), "testouilleur")
        self.assertEqual(str(profile), self.user.username)
        self.assertEqual(prof_fav_city, "Zbeurg-en-Broute")
