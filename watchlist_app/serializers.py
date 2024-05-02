from rest_framework import serializers
from watchlist_app.models import WatchList,Review,StreamPlatform

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ('watchlist',)

class WatchListSerializer(serializers.ModelSerializer):
    platform = serializers.CharField(source='platform.name')

    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPLatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer()

    class Meta:
        model = StreamPlatform
        fields = "__all__"

