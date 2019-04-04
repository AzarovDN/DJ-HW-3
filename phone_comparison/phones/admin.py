from django.contrib import admin
from .models import ApplePhone, SamsungPone, PechenkaPhone


# class ApplePhoneAdmin(admin.ModelAdmin):
#     pass

admin.site.register(ApplePhone)
admin.site.register(SamsungPone)
admin.site.register(PechenkaPhone)