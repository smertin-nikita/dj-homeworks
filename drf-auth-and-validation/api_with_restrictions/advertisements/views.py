from django.db.models import Q
from rest_framework.permissions import IsAuthenticated, OR
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement, AdvertisementStatusChoices
from advertisements.permissions import IsStaffOrReadOnly, IsOwnerOrReadOnly
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter

    def get_queryset(self):
        """queryset с черновиками только для создателя"""
        user = self.request.user
        return Advertisement.objects.all().exclude(~Q(creator=user) & Q(status=AdvertisementStatusChoices.DRAFT))

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(),  OR(IsStaffOrReadOnly(), IsOwnerOrReadOnly())]
        return []
