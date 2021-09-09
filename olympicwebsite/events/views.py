from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets

from events.models import Events, MedalTally, Cheers
from events.serializers import EventsSerializers, MedalTallySerializers, CheersSerializers


class EventsScheduleList(viewsets.ModelViewSet):
    queryset = Events.objects.order_by('-event_date')
    serializer_class = EventsSerializers


class MedalTallyList(viewsets.ModelViewSet):
    queryset = MedalTally.objects.order_by('-medal')
    serializer_class = MedalTallySerializers


class CheersList(viewsets.ModelViewSet):
    queryset = Cheers.objects.all()
    serializer_class = CheersSerializers
