from rest_framework import generics
from config.permissions import AdminPermission
from .models import TrenerModel
from .serializer import TrenerSerializer
from rest_framework.pagination import PageNumberPagination


# Create your views here.
class AllTrenerView(generics.ListCreateAPIView):
    queryset = TrenerModel.objects.all()
    serializer_class = TrenerSerializer
    pagination_class = PageNumberPagination


class TrenerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrenerModel.objects.all()
    serializer_class = TrenerSerializer
    permission_classes = (AdminPermission,)
