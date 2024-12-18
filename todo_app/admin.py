from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'due_date', 'timestamp')
    list_filter = ('status', 'due_date', 'timestamp')
    search_fields = ('title', 'description', 'tags')
    readonly_fields = ('timestamp',)
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description')
        }),
        ('Timing', {
            'fields': ('timestamp', 'due_date')
        }),
        ('Status & Tags', {
            'fields': ('status', 'tags')
        }),
    )