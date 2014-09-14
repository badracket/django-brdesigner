from django.http import Http404
from myproject.brdesigner.models import Page

def gateway(request,path=""):
    pages = Page.objects.filter(is_active=True).order_by('display_order')

    for page in pages:
      if (page.url_pattern == path):
        return globals().get(page.page_type.view_controller)(request,page=page)

    raise Http404("URL not configured in Page admin")
