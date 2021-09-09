from rest_framework import serializers
from events.models import Events, MedalTally, Cheers


class EventsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'


class MedalTallySerializers(serializers.ModelSerializer):
    class Meta:
        model = MedalTally
        fields = '__all__'


class CheersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cheers
        fields = '__all__'
