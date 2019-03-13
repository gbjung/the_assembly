from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator
from django.shortcuts import render

from stories.models import StoryPage, Issue

def get_recent_stories(omit, paginate):
    query = StoryPage.objects.order_by('-id').filter(live=True)
    if omit:
        query = query.exclude(id=omit)

    return query[paginate:paginate+4]

@require_http_methods(["GET"])
def get_stories_by_category(category_id, paginate):
    category = Issue.objects.get(category_id)
    query = StoryPage.objects.child_of(category).order_by('date_published').filter(live=True)

    return query[paginate:paginate+10]

@require_http_methods(["GET"])
def issues_listing(request):
    issues_list = Issue.objects.all()
    paginator = Paginator(issues_list, 5)

    page = request.GET.get('page')
    issues = paginator.get_page(page)
    return render(request, 'stories/issues.html', {'issues': issues})
