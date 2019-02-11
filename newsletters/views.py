from django.views.generic.base import TemplateView


class NewsletterMakerView(TemplateView):

    template_name = "newsletter_maker.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
