from rest_framework import serializers
from items.models import Item, FavoriteItem
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['first_name', 'last_name']

class FavoriteSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	class Meta:
		model = FavoriteItem
		fields = ['user']

class ItemListSerializer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(
		view_name = "api-detail",
		lookup_field = "id",
		lookup_url_kwarg = "item_id"
		)

	added_by = UserSerializer()
	fav_by = serializers.SerializerMethodField()

	class Meta:
		model = Item
		fields = ['image', 'name', 'detail', 'added_by', 'fav_by']

	def get_fav_by(self, obj):
		favs = FavoriteItem.objects.filter(item=obj)
		user_count = favs.count()
		return user_count


class ItemDetailSerializer(serializers.ModelSerializer):
	fav_by = serializers.SerializerMethodField()

	class Meta:
		model = Item
		fields = ['image', 'name', 'description', 'fav_by']

	def get_fav_by(self, obj):
		return FavoriteSerializer(obj.favoriteitem_set.all(), many=True).data


