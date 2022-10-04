from django.contrib import admin

# Register your models here.
from .models import Ticket, User

admin.site.register(Ticket)
admin.site.register(User)
