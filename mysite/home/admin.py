from django.contrib import admin
from home.models import Visitor
from home.models import Prisoner
from home.models import Guard

admin.site.register(Visitor)
admin.site.register(Prisoner)
admin.site.register(Guard)