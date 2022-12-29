from django.contrib import admin
from .models import Card, Info


class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'seria', 'nomer', 'date_start', 'date_end', 'summa', 'srok', 'status')


class InfoAdmin(admin.ModelAdmin):
    list_display = ('card', 'change', 'value')


admin.site.register(Card, CardAdmin)
admin.site.register(Info, InfoAdmin)
