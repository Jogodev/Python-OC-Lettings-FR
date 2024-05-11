from django.urls import path
import profiles.views

urlpatterns = [
    path("profiles/", profiles.views.index, name="profiles_index"),
    path("profiles/<str:username>/", profiles.views.profile, name="profile"),
]
