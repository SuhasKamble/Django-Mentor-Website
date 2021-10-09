
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("about", views.about, name="About"),
    path("courses", views.courses, name="Courses"),
    path("contact", views.contact, name="Contact"),
    path("events", views.events, name="Events"),
    path("pricing", views.pricing, name="Pricing"),
    path("trainers", views.trainers, name="Trainers"),
]
