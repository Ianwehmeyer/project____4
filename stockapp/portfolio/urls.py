from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('calc', views.calc),
    path('ajaxform', views.home),
    path('ajax', views.handleAjax),
    path('login', views.login_view),
    path('logout', views.logout_view),
]
