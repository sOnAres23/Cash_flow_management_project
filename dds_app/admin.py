from django.contrib import admin
from .models import Type, Status, Category, Subcategory, Record


class RecordAdmin(admin.ModelAdmin):
    list_display = ('date', 'status', 'type', 'category', 'subcategory', 'amount', 'comment')
    list_filter = ('status', 'type', 'category', 'subcategory')


admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Record, RecordAdmin)
