from django.urls import path, include
from rest_framework import routers

from events.views import EventsScheduleList, MedalTallyList, CheersList

router = routers.DefaultRouter()
router.register(r'events_schedule', EventsScheduleList)
router.register(r'medal_tally', MedalTallyList)
router.register(r'fanzone', CheersList)


urlpatterns = [
    path('', include(router.urls)),
    path('events_schedule/',
         EventsScheduleList.as_view({'get': 'list'}), name='events-schedule'),
    path('medal_tally/',
         MedalTallyList.as_view({'get': 'list'}), name='medal-tally'),
    path('fanzone/',
         CheersList.as_view({'get': 'list'}), name='fanzone-cheers'),
]
