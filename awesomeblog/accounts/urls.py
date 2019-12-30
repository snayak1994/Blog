from django.conf.urls import url
from views import  UserRegisterView
urlpatterns = [
    url(r'^register/',UserRegisterView.as_view(),name='register'),
    url(r'^login/',UserRegisterView.as_view(),name='login'),
]