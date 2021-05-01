from rest_framework import serializers


from .models import usageRate


class usageRateSerializer(serializers.ModelSerializer):

    class Meta:
        model = usageRate
        fields = ['usageField','usageRate']
        #['city','_year', 'waterCapita']
