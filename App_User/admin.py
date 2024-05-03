from django.contrib import admin
from .models import ContactUs

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('come_time', 'sender_firstname', 'sender_lastname', 'sender_email', 'message')


admin.site.register(ContactUs, ContactAdmin)
