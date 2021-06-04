from django.urls import path
from . import views

app_name = 'tryviubox'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    # path('/sign_s3', views.sign_s3, name='sign-s3'),
]
