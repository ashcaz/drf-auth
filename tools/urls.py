from django.urls import path
from .views import ToolListView, ToolDetailView

urlpatterns = [
    path("", ToolListView.as_view(), name="tool_list"),
    path("<int:pk>/", ToolDetailView.as_view(), name="tool_detail"),
]