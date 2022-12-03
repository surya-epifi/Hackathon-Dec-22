from django.contrib import admin

# Register your models here.
from ScammerHuntCore.models import *

admin.site.register(ScrapeData)
admin.site.register(Scammer)
admin.site.register(Keywords)
admin.site.register(PriorityUser)
