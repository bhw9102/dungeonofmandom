from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from session.models import Player, Room, RoomPlayer


class PlayerAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name', )


class RoomAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', )
    list_display_links = ('id', 'name', )


class RoomPlayerAdmin(ImportExportModelAdmin):
    list_display = ('id', '__str__', 'created_at')
    list_display_links = ('id', '__str__', )


admin.site.register(Player, PlayerAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(RoomPlayer, RoomPlayerAdmin)
