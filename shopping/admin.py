from django.contrib import admin
from .models import item, user
# Register your models here.
# admin.site.register(item)

admin.site.register(user)
@admin.register(item)
class itemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'author')
    list_filter = ('price', 'name')
