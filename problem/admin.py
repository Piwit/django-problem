from django.contrib import admin

from .models import Problem


class ProblemAdmin(admin.ModelAdmin):
    model = Problem
    list_display = ('user', 'page', 'reported_at', 'resolved_at', 'resolved')
    list_filter = ('page', 'reported_at', 'resolved_at', 'resolved')
    search_fields = ('problem', 'page')
    date_hierarchy = 'reported_at'

admin.site.register(Problem, ProblemAdmin)
