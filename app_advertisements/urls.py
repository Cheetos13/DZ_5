from django.urls import path

from .views import example, top_sellers


urlpatterns = [
    path("", example),
    path("example.html", example, name="main-page"),
    path("top-sellers.html", top_sellers, name="top-sellers")

]
