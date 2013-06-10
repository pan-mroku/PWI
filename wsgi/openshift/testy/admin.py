from django.contrib import admin
from models import StringTest


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
(None,{"fields": ["value"]}),("Date information", {"fields": ["pub_date"]})]
    list_display = ("value", "pub_date")
    list_filter = ["pub_date"]
    search_fields = ["value"]
    date_hierarchy = "pub_date"





admin.site.register(StringTest, PollAdmin)