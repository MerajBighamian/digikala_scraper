from django.urls import path
from .views import GetUrlAndListData

app_name = "apis"
urlpatterns = [
    path('',GetUrlAndListData.as_view(),name='index')
]