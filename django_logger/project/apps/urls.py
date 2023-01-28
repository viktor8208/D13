from django.urls import path, include
from apps.views import login_view
urlpatterns = [

    path('apps/', login_view),
    ]