import sentry_sdk
from django.shortcuts import render

from .models import Letting


# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit. Sed non
# placerat massa. Integer est nunc, pulvinar a tempor et, bibendum id arcu. Vestibulum
# ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae;
# Cras eget scelerisque
def index(request):
    """Letting's main page.
    Displays all the available lettings (list of the titles)."""
    try:
        lettings_list = Letting.objects.all()
        context = {"lettings_list": lettings_list}
        return render(request, "lettings/index.html", context)
    except Exception as err:
        sentry_sdk.capture_message(f"500 error: {err} {request}")
        # sentry_sdk.capture_exception(err)
        return render(request, "500.html")


# Cras ultricies dignissim purus, vitae hendrerit ex varius non. In accumsan porta nisl
# id eleifend. Praesent dignissim, odio eu consequat pretium, purus urna vulputate arcu,
# vitae efficitur lacus justo nec purus. Aenean finibus faucibus lectus at porta. Maecenas
# auctor, est ut luctus congue, dui enim mattis enim, ac condimentum velit libero in magna.
# Suspendisse potenti. In tempus a nisi sed laoreet. Suspendisse porta dui eget sem accumsan
# interdum. Ut quis urna pellentesque justo mattis ullamcorper ac non tellus. In tristique
# mauris eu velit fermentum, tempus pharetra est luctus. Vivamus consequat aliquam libero,
# eget bibendum lorem. Sed non dolor risus. Mauris condimentum auctor elementum. Donec quis
# nisi ligula. Integer vehicula tincidunt enim, ac lacinia augue pulvinar sit amet.
def letting(request, letting_id):
    """Displays the details of a selected letting.
    In case of an error, send a message to Sentry and
    returns the Error 500 page."""
    try:
        letting = Letting.objects.get(id=letting_id)
        context = {
            "title": letting.title,
            "address": letting.address,
        }
        return render(request, "lettings/letting.html", context)
    except Exception as err:
        sentry_sdk.capture_message(f"500 error: {err} {request}")
        # sentry_sdk.capture_exception(err)
        return render(request, "500.html")
