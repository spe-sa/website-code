from django.utils import timezone
from django.core.urlresolvers import reverse
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from cms.models import CMSPlugin
# using taggit for all our tagging
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase

from mainsite.models import Tier1Discipline
from mainsite.models import Topics
import sys

ORDER_BY = (
    ("-article_hits", 'Most Read'),
    ("-date", 'Most Recent'),
)

DEFAULT_PLUGIN_TEMPLATE = 'spe_blog/plugins/image_left.html'
PLUGIN_TEMPLATES = (
    (DEFAULT_PLUGIN_TEMPLATE, 'Image on left'),
    ('spe_blog/plugins/overlay.html', 'Image with caption overlay'),
    ('spe_blog/plugins/picture_with_text_below.html', 'Image with text below'),
    ('spe_blog/plugins/compact_left_image.html', 'Compact Image on left'),
)

DEFAULT_ISSUE_TEMPLATE = 'spe_blog/plugins/issue_channel.html'
ISSUE_TEMPLATES = (
    (DEFAULT_ISSUE_TEMPLATE, 'Issues listing'),
    ('spe_blog/plugins/issue_sidebar.html', 'Subscribe & read issue'),
)

DEFAULT_EDITORIAL_TEMPLATE = 'spe_blog/plugins/editorial.html'
EDITORIAL_TEMPLATES = (
    (DEFAULT_EDITORIAL_TEMPLATE, 'Editorial'),
)


# Moved to tables
# PUBS =(
#     ('JPT', 'Journal of Petroleum Technology'),
#     ('TWA', 'The Way Ahead'),
#     ('OGF', 'Oil and Gas Facilities'),
#     ('HSE', 'HSE Now'),
#     ('WWW', 'Online'),
# )
# DISCIPLINES =(
#     ('D&C', 'Drilling and Completions'),
#     ('HSE', 'Health, Safety, Security, Environment & Social Responsibility'),
#     ('M&I', 'Management & Information'),
#     ('P&O', 'Production & Operations'),
#     ('PFC', 'Projects, Facilities & Construciton'),
#     ('RDD', 'Reservoir Description & Dynamics'),
#     ('UND', 'Undeclared'),
# )


class Tagged(TaggedItemBase):
    content_object = models.ForeignKey("Article")


class TaggedAuto(TaggedItemBase):
    content_object = models.ForeignKey("Article")


class Publication(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=150, unique=True)
    subscription_url = models.URLField(verbose_name=u'Subscription URL', blank=True, null=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.code + ": " + self.name

class Issue(models.Model):
    publication = models.ForeignKey(Publication)
    date = models.DateField(verbose_name='Publication Date', blank=True, null=True)
    print_volume = models.PositiveIntegerField(blank=True, null=True)
    print_issue = models.PositiveIntegerField(blank=True, null=True)
    cover = models.ImageField(upload_to='covers')
    issue_url = models.URLField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.publication.name

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Category")

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.name


class Article(models.Model):
    # NOTE: add blank=True if we can have articles not assigned to a publication
    publication = models.ForeignKey(Publication)
    print_volume = models.PositiveIntegerField(blank=True, null=True)
    print_issue = models.PositiveIntegerField(blank=True, null=True)
    sponsored = models.BooleanField(default=False)
    free = models.BooleanField(default=False)
    free_start = models.DateField(verbose_name='Start Date', default=timezone.now)
    free_stop = models.DateField(verbose_name='End Date', default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100, unique_for_month='date',
                            help_text='SEO Friendly name that is unique for use in URL', )
    teaser = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    introduction = models.TextField(blank=True, null=True,
                                    help_text=u'Introductory paragraph or \'teaser.\' for paywal')
    article_text = RichTextUploadingField(
        max_length=18000,
        help_text=u'Full text of the article.'
    )
    date = models.DateField(verbose_name='Publication Date', default=timezone.now)
    #    discipline = models.CharField(max_length = 4, choices=DISCIPLINES)
    picture = models.ImageField(upload_to='regular_images', blank=True, null=True, verbose_name=u'Picture for article')
    picture_alternate = models.CharField(max_length=50, blank=True, null=True, verbose_name=u'Picture alternate text')
    picture_caption = models.CharField(max_length=250, blank=True, null=True, verbose_name=u'Picture caption')
    picture_attribution = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'Picture attribution')
    article_hits = models.PositiveIntegerField(default=0, editable=False)
    article_last_viewed = models.DateTimeField(blank=True, null=True, editable=False)
    disciplines = models.ManyToManyField(Tier1Discipline, blank=True)

    # add taggit tags, auto-tags, and categories
    topics = models.ManyToManyField(Topics, verbose_name="Topic")

    tags = TaggableManager(verbose_name="Tags", through=Tagged, blank=True)
    tags.rel.related_name = "+"
    auto_tags = TaggableManager(verbose_name="Auto Tags", through=TaggedAuto, blank=True)
    auto_tags.rel.related_name = "+"

    class Meta:
        unique_together = ('publication', 'print_volume', 'print_issue', 'slug')
        ordering = ['-date', 'title']
        get_latest_by = ['date']

    def __unicode__(self):
        return str(self.publication.code) + ": " + self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'article_id': self.id})

class Editorial(models.Model):
    title_main = models.CharField(max_length=100, verbose_name="Main Title")
    title_sub = models.CharField(max_length=100, verbose_name="Sub-Title")
    exerpt = RichTextField(
        max_length=300,
        help_text=u'Exerpt'
    )
    picture = models.ImageField(upload_to='authors', blank=True, null=True, verbose_name=u'Picture of Author')
    picture_alternate = models.CharField(max_length=50, blank=True, null=True, verbose_name=u'Picture alternate text')
    picture_caption = models.CharField(max_length=250, blank=True, null=True, verbose_name=u'Picture caption')
    picture_attribution = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'Picture attribution')
    author_bio = RichTextField(
        max_length=500,
        help_text=u'Author Bio'
    )
    
    class Meta:
        verbose_name_plural = "Editorials"

    def __unicode__(self):
        buf = self.title_main + " - " + self.title_sub
        return buf


class ArticlesPlugin(CMSPlugin):
    template = models.CharField(max_length=255, choices=PLUGIN_TEMPLATES, default=DEFAULT_PLUGIN_TEMPLATE)
    articles = models.ManyToManyField(Article)
    order_by = models.CharField(
        max_length=20,
        choices=ORDER_BY,
        default="-article_hits"
    )
    # if user enters url and text then we display the show all link with these values
    # todo - change charfield to our URLField that takes relative paths
    all_url = models.CharField("Show All URL", max_length=250, blank=True, null=True)
    all_text = models.CharField("Show All Text", max_length=50, blank=True, null=True)

    def __unicode__(self):
        buf = self.get_order_by_display() + u" (%s)" % ', '.join([a.slug for a in self.articles.all()])
        return buf

    def copy_relations(self, old_instance):
        self.articles = old_instance.articles.all()

class EditorialPlugin(CMSPlugin):
    template = models.CharField(max_length=255, choices=EDITORIAL_TEMPLATES, default=DEFAULT_EDITORIAL_TEMPLATE)
    editorial = models.ManyToManyField(Editorial)
    lnk = models.URLField("Link URL", blank=True, null=True)

    def __unicode__(self):
        return "Editorial Plugin"

    def copy_relations(self, old_instance):
        self.editorial = old_instance.editorial.all()
        self.articles = old_instance.articles.all()

# class ArticlePlugin(CMSPlugin):
#     template = models.CharField(max_length=255, choices=PLUGIN_TEMPLATES, default=DEFAULT_PLUGIN_TEMPLATE)
#     article = models.ForeignKey(Article, on_delete=models.PROTECT)
#     # if user enters url and text then we display the show all link with these values
#     # todo - change charfield to our URLField that takes relative paths
#     all_url = models.CharField("Show All URL", max_length=250, blank=True, null=True)
#     all_text = models.CharField("Show All Text", max_length=50, blank=True, null=True)
#
#     def __unicode__(self):
#         return u"%s" % self.article
#
#
class ArticlesListingPlugin(CMSPlugin):
    # display
    template = models.CharField(max_length=255, choices=PLUGIN_TEMPLATES, default=DEFAULT_PLUGIN_TEMPLATE)
    cnt = models.PositiveIntegerField(default=5, verbose_name=u'Number of Articles')
    order_by = models.CharField(max_length=20, choices=ORDER_BY, default="-article_hits")
    starting_with = models.PositiveIntegerField(default=1)
    # limit to
    publication = models.ForeignKey(Publication, blank=True, null=True)
    personalized = models.BooleanField(default=True)
    discipline = models.ForeignKey(Tier1Discipline, blank=True, null=True)
    category = models.ForeignKey(Category, blank=True, null=True)
    # if user enters url and text then we display the show all link with these values
    all_url = models.URLField("Show All URL", blank=True, null=True)
    all_text = models.CharField("Show All Text", max_length=50, blank=True, null=True)

    def __unicode__(self):
        dictionary = dict(PLUGIN_TEMPLATES)
        buf = "(" + str(self.starting_with) + " - " + str(self.cnt + self.starting_with - 1) + ") by " + self.get_order_by_display()
        if self.discipline:
            buf += " (" + self.discipline.code + ")"
        if self.personalized:
            buf += " personalized"
        if self.category:
            buf += " (" + self.category.name + " only)"
        buf += " using " + dictionary[self.template]
        return buf

class IssuesByPublicationPlugin(CMSPlugin):
    template = models.CharField(max_length=255, choices=ISSUE_TEMPLATES, default=DEFAULT_ISSUE_TEMPLATE)
    cnt = models.PositiveIntegerField(default=5, verbose_name=u'Number of Issues')
    starting_with = models.PositiveIntegerField(default=1)
    publication = models.ForeignKey(Publication)
    active = models.BooleanField(default=True)
    all_url = models.URLField("Show All URL", blank=True, null=True)
    all_text = models.CharField("Show All Text", max_length=50, blank=True, null=True)

    def __unicode__(self):
        dictionary = dict(ISSUE_TEMPLATES)
        buf = " - " + self.publication.name + " - " + str(self.cnt) + " issues, starting "
        if self.starting_with > 1:
            buf += str(self.starting_with) + " back"
        else:
            buf += "with the newest"
        buf += " using " + dictionary[self.template]
        return buf
