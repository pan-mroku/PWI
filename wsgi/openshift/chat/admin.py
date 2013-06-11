from django.contrib import admin
from models import Message, User

class ChoiceInline(admin.TabularInline):
    model = User
    extra = 1


class MessageAdmin(admin.ModelAdmin):
    fieldsets = [
(None,{"fields": ["message"]}),("Date information", {"fields": ["timestamp"]})]
    list_display = ("message", "timestamp")
    list_filter = ["timestamp"]
    search_fields = ["message"]
    date_hierarchy = "timestamp"
    inlines = [ChoiceInline]





admin.site.register(Message, MessageAdmin)