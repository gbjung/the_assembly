from base.models import Author, StoryCategory
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)

class PeopleModelAdmin(ModelAdmin):
    model = Author
    menu_label = 'Authors'  # ditch this to use verbose_name_plural from model
    menu_icon = 'fa-users'  # change as required
    list_display = ('first_name', 'last_name', 'title', 'thumb_image')

class StoryCategoryModelAdmin(ModelAdmin):
    model = StoryCategory
    menu_label = 'Story Categories'  # ditch this to use verbose_name_plural from model
    menu_icon = 'fa-comments'  # change as required
    list_display = ('name', 'thumb_image')

modeladmin_register(PeopleModelAdmin)
modeladmin_register(StoryCategoryModelAdmin)
