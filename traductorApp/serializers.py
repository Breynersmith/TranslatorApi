from rest_framework import serializers


class TraductorSerializers(serializers.Serializer):
  text = serializers.CharField(max_length=500)
  destine = serializers.CharField(max_length=509, default='en')
  