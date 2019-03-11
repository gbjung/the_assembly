from django.views.decorators.http import require_http_methods

from stories.models import StoryPage, StoryCategory

def get_recent_stories(omit, paginate):
    query = StoryPage.objects.order_by('-id')
    if omit:
        query = query.exclude(id=omit)

    return query[paginate:paginate+4]

@require_http_methods(["GET"])
def get_stories_by_category(category_id, paginate):
    category = StoryCategory.objects.get(category_id)
    query = StoryPage.objects.child_of(category).order_by('date_published').filter(live=True)

    return query[paginate:paginate+10]
