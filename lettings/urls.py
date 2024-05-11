from django.urls import path
import lettings.views

urlpatterns = [
    path("lettings/", lettings.views.index, name="lettings_index"),
    path("lettings/<int:letting_id>/", lettings.views.letting, name="letting"),
]
