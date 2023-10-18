from django.contrib import admin

from .models import Choice, Question, Image

# Register your models here.

admin.site.register(Question)

admin.site.register(Choice)
class imageAdmin (admin.ModelAdmin):
    list_display = ["title", "photo"]

admin.site.register(Image, imageAdmin)