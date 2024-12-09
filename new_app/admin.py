from django.contrib import admin

from new_app import models

# Register your models here.
admin.site.register(models.Login)
admin.site.register(models.Counsiler)
admin.site.register(models.Patient)
admin.site.register(models.Request)
admin.site.register(models.feedback)
admin.site.register(models.feedback_c)