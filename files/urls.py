from django.urls import path
from .views import DbPageView,ReactPageView,PostCreateView,PostUpdateView,PostDeleteView

urlpatterns = [
    path('dbview/<int:pk>/', DbPageView.as_view(), name='dbview_post'),
    path('dbview/', DbPageView.as_view(), name='dbview'),
    path('react/',ReactPageView.as_view(), name='react'),
    path('post/', PostCreateView.as_view(), name='post'), 
    path('dbview/<int:pk>/edit/', PostUpdateView.as_view(), name='update'),
    path('dbview/<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
]