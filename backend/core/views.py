from .models import Car
from .serializers import CarSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import CursorPagination

class MyPag(CursorPagination):
    page_size = 10
    ordering = 'id'


class CarViewSet(ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    pagination_class = MyPag
    
    def filter_queryset(self, queryset):
        for k, v in self.request.query_params.items():
            if k == 'cursor':
                continue
            queryset = queryset.filter(**{k: v})
        return queryset

