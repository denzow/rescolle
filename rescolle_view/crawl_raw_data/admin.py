from django.contrib import admin
from .models import CrawlRawData


class CrawlRawDataAdmin(admin.ModelAdmin):
    fields = ['source', 'serial']


admin.site.register(CrawlRawData, CrawlRawDataAdmin)
