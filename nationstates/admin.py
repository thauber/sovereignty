from django.contrib import admin

from nationstates.models import *

class IssueChoiceInline(admin.TabularInline):
    model = IssueChoice

class IssueAdmin(admin.ModelAdmin):
    inlines = [IssueChoiceInline]

admin.site.register(Issue, IssueAdmin)