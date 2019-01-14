from base.models import Author
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)

class PeopleModelAdmin(ModelAdmin):
    model = Author
    menu_label = 'Authors'  # ditch this to use verbose_name_plural from model
    menu_icon = 'fa-users'  # change as required
    list_display = ('first_name', 'last_name', 'title', 'thumb_image')

modeladmin_register(PeopleModelAdmin)
