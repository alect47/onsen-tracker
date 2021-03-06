from rest_framework import serializers

from .models import Restaurant, Taco, Review, User

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class TacoSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.ReadOnlyField()

    class Meta:
        model = Taco
        fields = "__all__"


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    tacos = TacoSerializer(many=True, read_only=True)
    class Meta:
        model = Restaurant
        fields = ('id', 'yelp_id', 'name', 'phone', 'is_closed', 'review_count', 'yelp_rating', 'url', 'latitude', 'longitude', 'image_url', 'address', 'distance', 'tacoboutit_item_review_count', 'tacos')
