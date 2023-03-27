from rest_framework import serializers

from core.models import Organization, Holding


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = '__all__'


class OrganizationCreateSerializer(serializers.ModelSerializer):
    holding = serializers.CharField(max_length=255)

    class Meta:
        model = Organization
        fields = '__all__'

    def create(self, validated_data):
        holding = Holding.objects.get(name=validated_data.get("holding"))
        print(validated_data)
        organization = Organization.objects.create(name=validated_data.get('name'), address=validated_data.get('address'),
                                                   holding=holding)
        return organization


    # def create(self, validated_data):
    #     holding = Holding.objects.get(name=validated_data.get('holding'))

