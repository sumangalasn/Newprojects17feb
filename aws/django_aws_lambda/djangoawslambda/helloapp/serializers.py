from rest_framework import serializers

from .models import Helloapp


class Hello:
  pass


class TodoSerializer(serializers.ModelSerializer):
  text = serializers.CharField(max_length=1000, required=True)

  def create(self, validated_data):

    return Hello.objects.create(
      text=validated_data.get('text')
    )

  def update(self, instance, validated_data):
    instance.text = validated_data.get('text', instance.text)
    instance.save()
    return instance

  class Meta:
    model = Hello
    fields = (
      'id',
      'text'
    )