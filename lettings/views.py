from django.shortcuts import render
from lettings.models import Letting
import logging

# Create your views here.


# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit.
# Sed non placerat massa. Integer est
# nunc, pulvinar a tempor et, bibendum id arcu.
# Vestibulum ante ipsum primis in faucibus orci luctus et ultrices
# posuere cubilia curae; Cras eget scelerisque
def index(request):
    """
    This view function handles the request to display all lettings.

    It retrieves all lettings from the database and passes them
    to the template for rendering.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object which renders
        the 'lettings/index.html' template with the context data.
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non.
# In accumsan porta nisl id eleifend. Praesent
# dignissim, odio eu consequat pretium, purus urna vulputate arcu,
# vitae efficitur lacus justo nec purus. Aenean
# finibus faucibus lectus at porta. Maecenas auctor, est ut luctus congue,
# dui enim mattis enim, ac condimentum velit
# libero in magna. Suspendisse potenti. In tempus a nisi sed laoreet.
# Suspendisse porta dui eget sem accumsan
# interdum. Ut quis urna pellentesque justo mattis ullamcorper ac non tellus.
# In tristique mauris eu velit fermentum,
# tempus pharetra est luctus. Vivamus consequat aliquam libero, eget bibendum lorem.
# Sed non dolor risus. Mauris
# condimentum auctor elementum. Donec quis nisi ligula. Integer vehicula tincidunt enim,
# ac lacinia augue pulvinar
# sit amet.
def letting(request, letting_id):
    """
    This view function handles the request to display a specific letting.

    It retrieves a letting with the given id from the database and passes
    it to the template for rendering.

    Args:
        request (HttpRequest): The request object.
        letting_id (int): The id of the letting to be displayed.

    Returns:
        HttpResponse: The response object which renders
        the 'lettings/letting.html' template with the context data.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
