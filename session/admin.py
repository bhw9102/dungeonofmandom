from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from session.models import Player, Room, RoomPlayer, Monster, Item, RemovedPackage


class PlayerAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name', )


class RoomAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', )
    list_display_links = ('id', 'name', )


class RoomPlayerAdmin(ImportExportModelAdmin):
    list_display = ('id', '__str__', 'created_at')
    list_display_links = ('id', '__str__', )


class MonsterAdmin(ImportExportModelAdmin):
    list_display = ('id', )
    list_display_links = ('id', )


class ItemAdmin(ImportExportModelAdmin):
    list_display = ('id', )
    list_display_links = ('id', )


class RemovedPackageAdmin(ImportExportModelAdmin):
    list_display = ('id', )
    list_display_links = ('id', )


admin.site.register(Player, PlayerAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(RoomPlayer, RoomPlayerAdmin)
admin.site.register(Monster, MonsterAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(RemovedPackage, RemovedPackageAdmin)
