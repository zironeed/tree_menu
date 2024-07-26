from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'menu_app/index.html'
