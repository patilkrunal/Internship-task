from django.contrib import admin

# Register your models here.
from events.models import Events, MedalTally, Cheers

admin.site.register(Events)
admin.site.register(MedalTally)
admin.site.register(Cheers)
