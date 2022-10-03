from rest_framework import serializers
from .models import Urls
class UrlSerializer(serializers.ModelSerializer):
    """
    this is class for serilizing data from Urls model
    """
    class Meta:
        model = Urls
        fields = "__all__"