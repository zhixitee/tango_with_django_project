from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile
# Register your models here.


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slugs': ('name',)}


admin.site.register(Category)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
