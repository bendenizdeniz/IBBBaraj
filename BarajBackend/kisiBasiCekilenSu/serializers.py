from rest_framework import serializers


from .models import WaterperCapita


class WaterCapitaSerializer(serializers.ModelSerializer):

    class Meta:
        model = WaterperCapita
        fields = '__all__'
        #['city','_year', 'waterCapita']
