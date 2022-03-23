from django.urls import path
from django.urls.resolvers import URLPattern
from mainApp import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("shop", views.ShopView.as_view(), name="shop"),
    path("help", views.HelpView.as_view(), name='help'),
    path("about", views.AboutView.as_view(), name="about"),
    path("", views.basket_add, name="basket_add")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

handler404 = 'mainApp.views.handler404'
