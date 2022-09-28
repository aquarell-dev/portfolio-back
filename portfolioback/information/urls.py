from django.urls import path

from .views import InfoListView

urlpatterns = [
    path('abouts/', InfoListView.as_view())
]
