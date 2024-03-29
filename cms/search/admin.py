from django.contrib import admin
from search.models import SearchKeyword
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

class SearchKeywordInline(admin.TabularInline):
    model = SearchKeyword
    extra = 3

class FlatPageAdminWithKeyword(FlatPageAdmin):
    inlines = [SearchKeywordInline]

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdminWithKeyword)