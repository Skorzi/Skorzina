from django.urls import path
from django.urls.resolvers import URLPattern
from mainApp import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView


urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("shop", views.ShopView.as_view(), name="shop"),
    path("help", views.HelpView.as_view(), name='help'),
    path("about", views.AboutView.as_view(), name="about"),
    path("basket_add", views.basket_add, name="basket_add"),
    path("basket_remove", views.basket_remove, name="basket_remove"),
    path("product/<int:pk>", views.ProductView.as_view(), name="product"),
    path("register", views.RegisterView.as_view(), name='register'),
    path('login', views.login_view, name='login_view'),
    path('logout', views.logout_view, name='logout_view'),
    # path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('activate', views.activate, name='activate'),
    path('confirmReg', views.confirmReg, name='confirmReg'),
    path('changePassword', PasswordResetView.as_view(template_name="mainApp/changePassword.html"), name='changePassword'),
    path('password_reset_done', PasswordResetDoneView.as_view(template_name='mainApp/changePasswordHelpText.html'), name='password_reset_done'),
    path('', views.IndexView.as_view(), name='password_reset_complete'),
    path('password_reset_confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name='mainApp/changePasswordEmail.html'), name='password_reset_confirm'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

handler404 = 'mainApp.views.handler404'
