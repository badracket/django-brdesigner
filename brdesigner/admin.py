from django import forms
from django.contrib import admin
from myproject.brdesigner.models import *
from django.utils.safestring import mark_safe

class BadRacketAdminBase(admin.ModelAdmin):
    class Media:
        js = (
            'brdesigner/js/admin_list_reorder.js',
            'brdesigner/js/tinymce/tinymce.min.js',
            'brdesigner/js/textareas.js',
        )

    
class SortableMenuItemAdmin(BadRacketAdminBase):
    list_display = ["id","display_name","target_page","external_link","is_active","rel","target","display_order"]
    list_display_links = ["id"]
    list_editable = ["display_name","target_page","external_link","is_active","rel","target","display_order"]

class SortablePageAdmin(BadRacketAdminBase):
    list_display = ["id","name","title","url_pattern","page_type","is_active","display_order"]
    list_display_links = ["id"]
    list_editable = ["name","title","url_pattern","page_type","is_active","display_order"]


admin.site.register(PageType)
admin.site.register(MenuItem, SortableMenuItemAdmin)
admin.site.register(Page, SortablePageAdmin)
