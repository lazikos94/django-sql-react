from django.urls import path
from .views import DbPageView,ReactPageView

urlpatterns = [
    path('dbview/', DbPageView.as_view(), name='dbview'),
    path('react/',ReactPageView.as_view(), name='react')
]