from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Card
from .serializers import CardSerializer
from core.permissions import IsOwnerOrReadOnly


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # Cache requested url for each user for 2 hours
    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 60 * 2))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


    # def get_permissions(self):
    #     if self.action == 'create':
    #         return [AllowAny()]
    #     elif self.action in ['update', 'destroy']:
    #         return [IsOwnerOrReadOnly()]
    #
    #     return super().get_permissions()

