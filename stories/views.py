from stories.models import StoryPage


def get_recent_stories(omit, paginate):
    query = StoryPage.objects.order_by('-id')
    if omit:
        query.exclude(id=omit)

    return query[paginate:paginate+4]
