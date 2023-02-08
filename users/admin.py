from django.contrib import admin
from .models.users import User
from .models.countries import Country

admin.site.register(User)
admin.site.register(Country)
