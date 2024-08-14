from django.shortcuts import render
from profiles.models import Profile
import logging

# Create your views here.


# Sed placerat quam in pulvinar commodo. Nullam
# laoreet consectetur ex
# , sed consequat libero pulvinar eget. Fusc
# faucibus, urna quis auctor pharetra, massa
# dolor cursus neque, quis dictum lacus d
def index(request):
    """
    View function for displaying the index page.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML response containing the index page with a list of profiles.
    """
    try:
        profiles_list = Profile.objects.all()
        context = {"profiles_list": profiles_list}
        return render(request, "profiles/index.html", context)
    except Exception as e:
        logging.error(f"An unexpected error occurred while retrieving profiless: {e}")
        return render(request, "500.html", status=500)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam
# facilisis pharetra vulputate. Sed tincidunt, dolor
# id facilisis fringilla, eros leo tristique lacus,
# it. Nam aliquam dignissim congue. Pellentesque habitant
# morbi tristique senectus et netus et males
def profile(request, username):
    """
    View function to display the profile of a user.

    Args:
        request (HttpRequest): The HTTP request object.
        username (str): The username of the user whose profile is being viewed.

    Returns:
        HttpResponse: The HTTP response object containing the rendered profile template.
    """
    try:
        profile = Profile.objects.get(user__username=username)
        context = {"profile": profile}
        return render(request, "profiles/profile.html", context)
    except Profile.DoesNotExist:
        logging.error(f"Profile with username {username} does not exist.")
        return render(request, "404.html", status=404)
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return render(request, "500.html", status=500)
