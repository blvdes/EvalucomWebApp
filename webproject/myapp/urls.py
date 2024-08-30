from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("page/1", views.home, name="Home"),
    path("review/<int:IDParam>/", views.review, name="Review"),
    path("page/<int:pageNumber>", views.page, name="Page"),
    path("search", views.search, name="Search"),
    path("reviews", views.reviews, name="Reviews")
]