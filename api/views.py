from rest_framework.generics import ( ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView)
from items.models import Item, FavoriteItem
from .serializers import ItemListSerializer, ItemDetailSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsUser


class ItemListView(ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemListSerializer
	filter_backends = [OrderingFilter, SearchFilter,]
	search_fields = '__all__'
	permission_classes = [AllowAny,]


class ItemDetailView(RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'
	# permission_classes = [IsUser,]

