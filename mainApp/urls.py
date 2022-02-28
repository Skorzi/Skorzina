from django.urls import path
from django.urls.resolvers import URLPattern
from mainApp import views

urlpatterns = [
	path("", views.IndexView.as_view(), name="index")
]

