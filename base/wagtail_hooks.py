from authors.models import Author
from stories.models import Issue, StoryPage
from subscriptions.models import Subscriber
from newsletters.models import Newsletter
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from wagtail.core import hooks
from wagtail.admin.menu import MenuItem
from django.utils.safestring import mark_safe
from django.urls import reverse


class PeopleModelAdmin(ModelAdmin):
    model = Author
    menu_label = 'Authors'  # ditch this to use verbose_name_plural from model
    menu_icon = 'fa-users'  # change as required
    list_display = ('first_name', 'last_name', 'title', 'thumb_image', 'story_count')

class IssueModelAdmin(ModelAdmin):
    model = Issue
    menu_label = 'Issues'  # ditch this to use verbose_name_plural from model
    menu_icon = 'fa-comments'  # change as required
    list_display = ('title', 'date_published', 'child_stories_names')

class StoryModelAdmin(ModelAdmin):
    model = StoryPage
    menu_label = 'Stories'  # ditch this to use verbose_name_plural from model
    menu_icon = 'fa-pencil-square-o'  # change as required
    list_display = ('title', 'authors', 'category', 'tag_names', 'date_published')

class SubscriberModelAdmin(ModelAdmin):
    model = Subscriber
    menu_label = 'Subscribers'
    menu_icon = 'fa-hand-peace-o'
    list_display = ('email', 'join_date', 'is_active')

class NewsletterModelAdmin(ModelAdmin):
    model = Newsletter
    menu_label = 'Newsletters'
    menu_icon = 'fa-envelope-o'
    list_display = ('title', 'date', 'sent')

@hooks.register('register_admin_menu_item')
def add_newsletters_generator_menu_item():
    return MenuItem('Newsletter Generator', reverse('newsletter_maker'),
                    classnames='icon icon-fa-gear')


@hooks.register('construct_main_menu')
def hide_snippets_menu_item(request, menu_items):
    menu_items[:] = [item for item in menu_items if item.name not in ['snippets', 'documents']]

modeladmin_register(StoryModelAdmin)
modeladmin_register(PeopleModelAdmin)
modeladmin_register(IssueModelAdmin)
modeladmin_register(SubscriberModelAdmin)
modeladmin_register(NewsletterModelAdmin)
