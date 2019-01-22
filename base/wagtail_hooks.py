from base.models import Author, StoryCategory
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from wagtail.core import hooks

class PeopleModelAdmin(ModelAdmin):
    model = Author
    menu_label = 'Authors'  # ditch this to use verbose_name_plural from model
    menu_icon = 'fa-users'  # change as required
    list_display = ('first_name', 'last_name', 'title', 'thumb_image', 'story_count')

class StoryCategoryModelAdmin(ModelAdmin):
    model = StoryCategory
    menu_label = 'Story Categories'  # ditch this to use verbose_name_plural from model
    menu_icon = 'fa-comments'  # change as required
    list_display = ('name', 'thumb_image', 'child_stories')

@hooks.register('construct_main_menu')
def hide_snippets_menu_item(request, menu_items):
  menu_items[:] = [item for item in menu_items if item.name != 'snippets']

modeladmin_register(PeopleModelAdmin)
modeladmin_register(StoryCategoryModelAdmin)
