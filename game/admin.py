from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from game.models import HeroClass, ItemClass, MonsterClass


class HeroClassAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'health', 'desc', )
    list_display_links = ('id', 'name', )


class ItemClassAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'health', 'desc', )
    list_display_links = ('id', 'name', )


class MonsterClassAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'attack', 'desc', )
    list_display_links = ('id', 'name', )


admin.site.register(HeroClass, HeroClassAdmin)
admin.site.register(ItemClass, ItemClassAdmin)
admin.site.register(MonsterClass, MonsterClassAdmin)