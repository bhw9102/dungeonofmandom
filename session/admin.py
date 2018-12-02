from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from session.models import Player, Room, Round, RoomPlayer, Monster, Item, RemovedPackage


class PlayerAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name', )


class RoomAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', )
    list_display_links = ('id', 'name', )


class RoundAdmin(ImportExportModelAdmin):
    list_display = ('id', 'room', 'order', 'state', )
    list_display_links = ('id', )


class RoomPlayerAdmin(ImportExportModelAdmin):
    list_display = ('id', '__str__', 'created_at')
    list_display_links = ('id', '__str__', )


class MonsterAdmin(ImportExportModelAdmin):
    list_display = ('id', 'round', 'monster', 'order', 'place', )
    list_display_links = ('id', )


class ItemAdmin(ImportExportModelAdmin):
    list_display = ('id', 'round', 'item', 'place', )
    list_display_links = ('id', )


class RemovedPackageAdmin(ImportExportModelAdmin):
    list_display = ('id', 'round_player', 'monster', 'item')
    list_display_links = ('id', )


admin.site.register(Player, PlayerAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Round, RoundAdmin)
admin.site.register(RoomPlayer, RoomPlayerAdmin)
admin.site.register(Monster, MonsterAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(RemovedPackage, RemovedPackageAdmin)
