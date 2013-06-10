from django.contrib import admin
from models import Poll


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
(None,{"fields": ["question"]}),
("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),]


admin.site.register(Poll, PollAdmin)