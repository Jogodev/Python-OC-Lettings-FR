from django.shortcuts import render
import sentry_sdk


def custom_404_view(request, exception=None):
    """
    Custom view for handling 404 errors.

    Args:
        request (HttpRequest): The HTTP request object.
        exception (Exception, optional): The exception
        that triggered the 404 error. Defaults to None.

    Returns:
        HttpResponse: The rendered 404.html template with a 404 status code.
    """
    sentry_sdk.capture_message("A 404 error occurred", "error")
    return render(request, "404.html", status=404)


def custom_500_view(request):
    """
    Custom view for handling 500 server errors.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered response with the "500.html" template.
    """
    sentry_sdk.capture_message("A 500 error occurred", "error")
    return render(request, "500.html", {}, status=500)
