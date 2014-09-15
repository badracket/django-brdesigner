from django.http import Http404
from myproject.brdesigner.models import Page, MenuItem, BrandImages, JsFileLoad, CssFileLoad, CssSelector, GoogleAnalytics

def gateway(request,path=""):
    pages = Page.objects.filter(is_active=True).order_by('display_order')
    
    for page in pages:
      if (page.url_pattern == path):
        context = {}
        context['menu_item_list']     = MenuItem.objects.filter(is_active=True).order_by('display_order').all()
        context['brand_images']       = BrandImages.objects.filter(is_active=True).first()
        context['js_file_load_list']  = JsFileLoad.objects.filter(is_active=True).order_by('display_order').all()
        context['css_file_load_list'] = CssFileLoad.objects.filter(is_active=True).order_by('display_order').all()
        context['css_selector_list']  = CssSelector.objects.filter(is_active=True).all()
        context['google_analytics']   = GoogleAnalytics.objects.filter(is_active=True).first()
        context['page'] = page
        return globals().get(page.page_type.view_controller)(request,page=page,context=context)

    raise Http404("URL not configured in Page admin")
