from rest_framework import serializers


from .models import istanbulNufus


class istanbulNufusSerializer(serializers.ModelSerializer):

    class Meta:
        model = istanbulNufus
        fields = ['year', 'population']
