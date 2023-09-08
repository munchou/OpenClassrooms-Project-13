import sentry_sdk
from django.shortcuts import render

from .models import Profile


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed consequat libero
# pulvinar eget. Fusc faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis
# dictum lacus d
def index(request):
    """Profile's main page.
    Displays all the available user profiles (list of the usernames)."""
    try:
        profiles_list = Profile.objects.all()
        context = {"profiles_list": profiles_list}
        return render(request, "profiles/index.html", context)
    except Exception as err:
        sentry_sdk.capture_message(f"500 error: {err} {request}")
        # sentry_sdk.capture_exception(err)
        return render(request, "500.html")


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate. Sed tincidunt,
# dolor id facilisis fringilla, eros leo tristique lacus, it. Nam aliquam dignissim congue.
# Pellentesque habitant morbi tristique senectus et netus et males
def profile(request, username):
    """Displays the profile's details of a selected user."""
    try:
        profile = Profile.objects.get(user__username=username)
        context = {"profile": profile}
        return render(request, "profiles/profile.html", context)
    except Exception as err:
        sentry_sdk.capture_message(f"500 error: {err} {request}")
        # sentry_sdk.capture_exception(err)
        return render(request, "500.html")
