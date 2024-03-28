from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Role)
admin.site.register(UserRole)
admin.site.register(Key)
admin.site.register(Access)
admin.site.register(Permission)