from django.urls import path
from .views import DbPageView,TestPageView

urlpatterns = [
    path('dbview/', DbPageView.as_view(), name='dbview'),
    path('test/',TestPageView.as_view(), name='test')
]