from django.contrib import admin

from .models import Job, Qualifications, Requirements, Role, Tasks

admin.site.register(Job)
admin.site.register(Qualifications)
admin.site.register(Requirements)
admin.site.register(Role)
admin.site.register(Tasks)
# Register your models here.
