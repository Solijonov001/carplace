from django.contrib import admin

from common.models import MediaFile
# Register your models here.

@admin.register(MediaFile)
class MediaFIleAdmin(admin.ModelAdmin):
    list_display = ('file','car')
