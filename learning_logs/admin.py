from django.contrib import admin

# Register your models here.
from learning_logs import models


@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "text",
    )
    ordering = ("id",)
    list_per_page = 10
    list_max_show_all = 1000
