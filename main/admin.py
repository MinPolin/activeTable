from django.contrib import admin
from .models import Data


class DataAdmin(admin.ModelAdmin):
    list_display = ['base_id', 'status','fon_id' ]
    list_filter = ['status']
    search_fields = [field.name for field in Data._meta.fields]

    class Meta:
        model = Data


admin.site.register(Data,DataAdmin)
