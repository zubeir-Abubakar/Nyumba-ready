# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Resident,Business,tags,Community

class BusinessAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)
# Register your models here.
admin.site.register(Resident)
admin.site.register(Business,BusinessAdmin)
admin.site.register(tags)
admin.site.register(Community)
