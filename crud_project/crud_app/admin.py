from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_number', 'first_name', 'last_name', 'email', 'phone', 'enrollment_date')
    list_filter = ('enrollment_date', 'date_of_birth')
    search_fields = ('first_name', 'last_name', 'email', 'roll_number')
    readonly_fields = ('enrollment_date',)
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'date_of_birth', 'address')
        }),
        ('Academic Information', {
            'fields': ('roll_number', 'enrollment_date')
        }),
    )
