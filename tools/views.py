from tools.permissions import IsOwnerOrReadOnly
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializer import ToolSerializer
from .models import Tool


class ToolListView(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer


class ToolDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer
