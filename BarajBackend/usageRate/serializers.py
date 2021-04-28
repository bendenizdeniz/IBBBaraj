from rest_framework import serializers


from .models import usageRate


class usageRateSerializer(serializers.ModelSerializer):

    class Meta:
        model = usageRate
        fields = '__all__'
        #['city','_year', 'waterCapita']
