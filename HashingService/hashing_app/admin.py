from django.contrib import admin
from hashing_app.models import RequestLog


class RequestLogAdmin(admin.ModelAdmin):
    pass


admin.site.register(RequestLog, RequestLogAdmin)
