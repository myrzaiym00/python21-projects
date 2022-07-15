from abstract.serializers import BaseSerializer
from .models import Car, Comment

class Car_serializer(BaseSerializer):
    class Meta:
        fields = ["id", "brand", "model", "year", "engine_volume", "color", "body_type", "mileage", "price", "likes"]
        queryset = Car.objects

    def serialize_obj(self, obj):
        dict_ = super().serialize_obj(obj)
        dict_["comments"] = CommentSerializer().serialize_queryset(obj.comments)
        return dict_

class CommentSerializer(BaseSerializer):
    class Meta:
        fields = ["body", "created_at"]
        queryset = Comment.objects

    def serialize_obj(self, obj):
        from datetime import datetime
        dict_ =  super().serialize_obj(obj)
        dict_["user"] = obj.user.email
        dict_['created_at'] = obj.created_at.strftime("%d.%m.%Y %H:%M:%S")
        return dict_