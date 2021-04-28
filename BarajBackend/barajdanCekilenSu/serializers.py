from rest_framework import serializers


from .models import damVolume


class damVolumeSerializer(serializers.ModelSerializer):

    class Meta:
        model = damVolume
        fields = '__all__'
        #['city','_year', 'waterCapita']
