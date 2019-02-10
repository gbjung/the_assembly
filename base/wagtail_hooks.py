from authors.models import Author
from stories.models import StoryCategory, StoryPage
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
    list_display = ('title', 'thumb_image', 'child_stories')

class StoryModelAdmin(ModelAdmin):
    model = StoryPage
    menu_label = 'Stories'  # ditch this to use verbose_name_plural from model
    menu_icon = 'fa-pencil-square-o'  # change as required
    list_display = ('title', 'authors', 'category', 'tag_names', 'date_published')

@hooks.register('construct_main_menu')
def hide_snippets_menu_item(request, menu_items):
    menu_items[:] = [item for item in menu_items if item.name not in ['snippets', 'documents']]

modeladmin_register(StoryModelAdmin)
modeladmin_register(PeopleModelAdmin)
modeladmin_register(StoryCategoryModelAdmin)
