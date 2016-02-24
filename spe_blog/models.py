from django.db import models
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from django.utils import six
from django.utils.encoding import python_2_unicode_compatible, force_text
from django.utils.functional import lazy
from django.utils.translation import ugettext_lazy as _, string_concat

from cms.models import CMSPlugin
# using taggit for all our tagging
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase
from mainsite.models import Discipline

DISCIPLINES =(
    ('D&C', 'Drilling and Completions'),
    ('HSE', 'Health, Safety, Security, Environment & Social Responsibility'),
    ('M&I', 'Management & Information'),
    ('P&O', 'Production & Operations'),
    ('PFC', 'Projects, Facilities & Construciton'),
    ('RDD', 'Reservoir Description & Dynamics'),
    ('UND', 'Undeclared'),
)

ORDER_BY =(
    ("-article_hits", 'Most Read'),
    ("-date", 'Most Recent'),
)

PUBS =(
    ('JPT', 'Journal of Petroleum Technology'),
    ('TWA', 'The Way Ahead'),
    ('OGF', 'Oil and Gas Facilities'),
    ('HSE', 'HSE Now'),
    ('WWW', 'Online'),
)

PLUGIN_TEMPLATES = (
  ('spe_blog/plugins/image_left.html', 'Image on left'),
  ('spe_blog/plugins/overlay.html', 'Image with caption overlay'),
)

class Tagged(TaggedItemBase):
    content_object = models.ForeignKey("Article")

class TaggedAuto(TaggedItemBase):
    content_object = models.ForeignKey("Article")

class Article(models.Model):
    magazine = models.CharField(
        max_length = 4,
        choices = PUBS,
        default = "JPT",
        verbose_name="Magazine"
    )
    issue = models.PositiveIntegerField(default=1)
    article_number = models.PositiveIntegerField(default=1)
#    slug = models.SlugField(max_length=100, unique=True)
    title = models.CharField(max_length=250)
    subheading = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    introduction = models.TextField(
        help_text =u'Introductory paragraph or \'teaser.\''
    )
    article_text = RichTextUploadingField(
        max_length = 18000,
        help_text =u'Full text of the article.'
    )
    date = models.DateField()
#    discipline = models.CharField(max_length = 4, choices=DISCIPLINES)
    picture = models.ImageField(upload_to='regular_images', verbose_name = u'Picture for article')
    picture_alternate = models.CharField(max_length = 50, blank=True, null=True, verbose_name =u'Picture alternate text')
    picture_caption = models.CharField(max_length=250, blank=True, null=True, verbose_name = u'Picture caption')
    picture_attribution = models.CharField(max_length=255, blank=True, null=True, verbose_name = u'Picture attribution')
    article_hits = models.PositiveIntegerField(default = 0, editable=False)
    article_last_viewed = models.DateTimeField(blank=True, null=True, editable=False)
    disciplines = models.ManyToManyField(Discipline, blank=True)
    # add taggit tags, auto-tags, and categories
    tags = TaggableManager(verbose_name="Tags", through=Tagged, blank=True)
    tags.rel.related_name = "+"
    auto_tags = TaggableManager(verbose_name="Auto Tags", through=TaggedAuto, blank=True)
    auto_tags.rel.related_name = "+"

    class Meta:
        unique_together = (('magazine', 'issue', 'article_number',))

    def __unicode__(self):
        inf = self.magazine + " - " + self.title
        return inf

    def get_absolute_url(self):
        return reverse('detail', kwargs={'article_id':self.id})

class ArticleDisciplinePluginModel(CMSPlugin):
    title = models.CharField(max_length = 50)
    discipline = models.CharField(max_length = 4, choices=DISCIPLINES)
    articles = models.PositiveIntegerField(default=5)
    orderby = models.CharField(
        max_length = 20,
        choices = ORDER_BY,
        default = "-article_hits",
        verbose_name="Order by"
    )
    starting_with = models.PositiveIntegerField(
        default=0,
        verbose_name = u'Starting With'
    )

    def __unicode__(self):
        inf = ": " + self.title + "-" + self.discipline + " - " + str(self.articles)
        if self.orderby == "-article_hits":
            inf = inf + " entries - ordered by most read"
        if self.orderby == '-date':
            inf = inf + " entries - ordered by most recent"
        inf = inf + " - starting with item " + str(self.starting_with)
        return inf

class ArticleDisciplineByUserPluginModel(CMSPlugin):
    title = models.CharField(max_length = 50)
    articles = models.PositiveIntegerField(default=5)
    orderby = models.CharField(
        max_length = 20,
        choices = ORDER_BY,
        default = "-article_hits",
        verbose_name="Order by"
    )
    starting_with = models.PositiveIntegerField(
        default=0,
        verbose_name = u'Starting With'
    )

    def __unicode__(self):
        inf = ": " + self.title + "-" + str(self.articles)
        if self.orderby == '-article_hits':
            inf = inf + " entries - ordered by most read"
        if self.orderby == '-date':
            inf = inf + " entries - ordered by most recent"
        inf = inf + " - starting with item " + str(self.starting_with)
        return inf

class ArticleByPublicationPluginModel(CMSPlugin):
    title = models.CharField(max_length = 50)
    magazine = models.CharField(
        max_length = 4,
        choices = PUBS,
        default = "JPT",
        verbose_name="Magazine"
    )
    articles = models.PositiveIntegerField(default=5)
    orderby = models.CharField(
        max_length = 20,
        choices = ORDER_BY,
        default = "-article_hits",
        verbose_name="Order by"
    )
    starting_with = models.PositiveIntegerField(
        default=0,
        verbose_name = u'Starting With'
    )

    def __unicode__(self):
        inf = self.magazine + ": " + self.title + "-" + str(self.articles)
        if self.orderby == '-article_hits':
            inf = inf + " entries - ordered by most read"
        if self.orderby == '-date':
            inf = inf + " entries - ordered by most recent"
        inf = inf + " - starting with item " + str(self.starting_with)
        return inf

class SelectedFeatureArticlePluginModel(CMSPlugin):
    template = models.CharField(
        max_length = 255,
        choices = PLUGIN_TEMPLATES,
        verbose_name="Feature type"
    )
    magazine = models.CharField(
        max_length = 4,
        choices = PUBS,
        default = "JPT",
        verbose_name="From magazine"
    )
    issue = models.PositiveIntegerField(default=1)
    article_number = models.PositiveIntegerField(default=1, verbose_name=u'Article number')

    def __unicode__(self):
        act = dict(PLUGIN_TEMPLATES)
        inf = act[self.template] + " from " + self.magazine + " Issue " + str(self.issue) + " Article " + str(self.article_number)
        return inf
