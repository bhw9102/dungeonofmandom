from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from game.models import JobClass, EquipmentClass, MonsterClass


class JobClassAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'health', 'desc', )
    list_display_links = ('id', 'name', )


class EquipmentClassAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'health', 'desc', )
    list_display_links = ('id', 'name', )


class MonsterClassAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'attack', 'desc', )
    list_display_links = ('id', 'name', )


admin.site.register(JobClass, JobClassAdmin)
admin.site.register(EquipmentClass, EquipmentClassAdmin)
admin.site.register(MonsterClass, MonsterClassAdmin)