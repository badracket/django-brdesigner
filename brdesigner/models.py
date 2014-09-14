from django.db import models

class PageType(models.Model):
    name            = models.CharField(max_length=100)
    view_controller = models.CharField(max_length=100)
    
    def __unicode__(self):
        return '%s' % (self.name)

class Page(models.Model):
    name             = models.CharField(max_length=30)
    title            = models.CharField(max_length=30)
    url_pattern      = models.CharField(max_length=100, blank=True, null=True)
    page_type        = models.ForeignKey(PageType)
    is_active        = models.BooleanField()
    meta_description = models.CharField(max_length=1000, blank=True, null=True)
    meta_keywords    = models.CharField(max_length=1000, blank=True, null=True)
    use_alt_menu     = models.BooleanField()
    display_order    = models.PositiveSmallIntegerField("Position",blank=True, null=True)

    def __unicode__(self):
        return '%s' % (self.name)
    
    def save(self, *args, **kwargs):
        model = self.__class__
        
        if self.display_order is None:
            # Append
            try:
                last = model.objects.order_by('-display_order')[0]
                self.display_order = last.display_order + 1
            except IndexError:
                # First row
                self.display_order = 0
        
        return super(Page, self).save(*args, **kwargs)
    class Meta:
        ordering = ('display_order',)


class MenuItem(models.Model):
    display_name     = models.CharField(max_length=50)
    target_page      = models.ForeignKey(Page, blank=True, null=True)
    external_link    = models.CharField(max_length=50, blank=True, null=True)
    is_active        = models.BooleanField()
    rel              = models.CharField(max_length=50,blank=True, null=True)
    target           = models.CharField(max_length=50,blank=True, null=True)
    display_order    = models.PositiveSmallIntegerField("Position",blank=True, null=True)

    def __unicode__(self):
        return '%s' % (self.display_name)

    def save(self, *args, **kwargs):
        model = self.__class__

        if self.display_order is None:
            # Append
            try:
                last = model.objects.order_by('-display_order')[0]
                self.display_order = last.display_order + 1
            except IndexError:
                # First row
                self.display_order = 0

        return super(MenuItem, self).save(*args, **kwargs)
    class Meta:
        ordering = ['display_order']

class CssSelector(models.Model):
    selector         = models.CharField(max_length=100)

    def __unicode__(self):
        return '%s' % (self.selector)

class CssSetting(models.Model):
    property         = models.CharField(max_length=100)
    value            = models.CharField(max_length=100)
    selector         = models.ForeignKey(CssSelector)

    def __unicode__(self):
        return '%s: %s' % (self.property, self.value)

