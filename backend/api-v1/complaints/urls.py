from django.urls import path
from .views import ComplaintListView, ComplaintView, StatusView, ComplaintPostView

urlpatterns = [
    path('', ComplaintListView.as_view()),
    path('status', StatusView.as_view()),
    path('<pk>', ComplaintView.as_view()),
    path('create/<pk>', ComplaintPostView.as_view()),
]