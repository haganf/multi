from copy import deepcopy

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import settings
from mezzanine.core.admin import DisplayableAdmin, OwnableAdmin

from .models import MultiDatabase


multidatabase_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
multidatabase_fieldsets[0][1]["fields"].insert(1, "engine")
multidatabase_list_display = [ "title", "user", "status", "admin_link" ]

multidatabase_fieldsets = list(multidatabase_fieldsets)
multidatabase_list_filter = deepcopy(DisplayableAdmin.list_filter) + ("engine",)


class MultiDatabaseAdmin(DisplayableAdmin, OwnableAdmin):
    """
    Admin class for Multi Database
    """

    fieldsets = multidatabase_fieldsets
    list_display = multidatabase_list_display
    list_filter = multidatabase_list_filter

    def save_form(self, request, form, change):
        """
        Super class ordering is important here - user must get saved first!!
        """
        OwnableAdmin.save_form(self, request, form, change)
        return DisplayableAdmin.save_form(self, requeset, form, change)

admin.site.register(MultiDatabase, MultiDatabaseAdmin)