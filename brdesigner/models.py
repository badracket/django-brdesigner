from django.db import models

class SortableModel(models.Model):
    display_order    = models.PositiveSmallIntegerField("Position",blank=True, null=True)

    class Meta:
        ordering = ('display_order',)
        abstract=True

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

        return super(model, self).save(*args, **kwargs)

class PageType(models.Model):
    name            = models.CharField(max_length=100)
    view_controller = models.CharField(max_length=100)

    def __unicode__(self):
        return '%s' % (self.name)

class Page(SortableModel):
    name             = models.CharField(max_length=30)
    title            = models.CharField(max_length=30)
    url_pattern      = models.CharField(max_length=100, blank=True, null=True)
    page_type        = models.ForeignKey(PageType)
    is_active        = models.BooleanField()
    meta_description = models.CharField(max_length=1000, blank=True, null=True)
    meta_keywords    = models.CharField(max_length=1000, blank=True, null=True)
    use_alt_menu     = models.BooleanField()

    def __unicode__(self):
        return '%s' % (self.name)


class MenuItem(SortableModel):
    display_name     = models.CharField(max_length=50)
    target_page      = models.ForeignKey(Page, blank=True, null=True)
    external_link    = models.CharField(max_length=50, blank=True, null=True)
    is_active        = models.BooleanField()
    rel              = models.CharField(max_length=50,blank=True, null=True)
    target           = models.CharField(max_length=50,blank=True, null=True)

    def __unicode__(self):
        return '%s' % (self.display_name)


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
