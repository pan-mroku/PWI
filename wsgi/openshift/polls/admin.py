from django.contrib import admin
from models import Poll, Choice


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
(None,{"fields": ["question"]}),
("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),]
    inlines = [ChoiceInline]


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


admin.site.register(Poll, PollAdmin)