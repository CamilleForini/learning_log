from django.contrib import admin

# Register your models here.
from learning_logs import models


@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "text",
        "date_added",
    )
    ordering = ("id",)
    list_per_page = 10
    list_max_show_all = 1000


@admin.register(models.Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "text",
        "topic",
        "date_added",
    )
    ordering = ("id",)
    list_per_page = 10
    list_max_show_all = 1000
