from django.contrib import admin

from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["name", "last_name", "author", "editor", "created_on", "updated_on"]


admin.site.register(Customer, CustomerAdmin)