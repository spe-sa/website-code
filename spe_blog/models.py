from django.utils import timezone
from django.core.urlresolvers import reverse
from django.db import models
from cms.models.fields import PageField
from cms.models import CMSPlugin
from cms.models import Page
from filer.fields.image import FilerImageField

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# using taggit for all our tagging
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase

from mainsite.models import Tier1Discipline
from mainsite.models import Topics
# from datetime import datetime
from mainsite.widgets import ColorPickerWidget

# import sys

DEFAULT_ORDER_BY = '-date'
ORDER_BY = (
    ("-article_hits", 'Most Read'),
    ("-date", 'Most Recent'),
)

DEFAULT_PLUGIN_TEMPLATE = 'spe_blog/plugins/image_left.html'
PLUGIN_TEMPLATES = (
    (DEFAULT_PLUGIN_TEMPLATE, 'Image on left'),
    ('spe_blog/plugins/overlay.html', 'Image with caption overlay'),
    ('spe_blog/plugins/picture_with_text_below.html', 'Image with text below'),
    ('spe_blog/plugins/picture_with_text_below_full.html', 'Image with text below full width'),
    ('spe_blog/plugins/person_of_interest.html', 'Persons of Interest'),
    ('spe_blog/plugins/carousel.html', 'Carousel'),
    ('spe_blog/plugins/side_list.html', 'Editorial Sidebar Article List'),
    ('spe_blog/plugins/side_feature.html', 'Editorial Sidebar'),
    ('spe_blog/plugins/article_editorial.html', 'Editorial w/ Author'),
    ('spe_blog/plugins/twa_articlebox.html', 'TWA Article Box'),
    ('spe_blog/plugins/twa_featured.html', 'TWA Featured Article Box'),
    # ('spe_blog/plugins/side_list.html', 'TWA Article List'),
)

DEFAULT_ISSUE_TEMPLATE = 'spe_blog/plugins/issue_channel.html'
ISSUE_TEMPLATES = (
    (DEFAULT_ISSUE_TEMPLATE, 'Issues listing'),
    ('spe_blog/plugins/issue_sidebar.html', 'Subscribe & read issue'),
    ('spe_blog/plugins/on_the_cover.html', 'On The Cover'),
)

DEFAULT_ISSUECOVER_TEMPLATE = 'spe_blog/plugins/on_the_cover.html'
ISSUECOVER_TEMPLATES = (
    (DEFAULT_ISSUECOVER_TEMPLATE, 'On The Cover'),
    ('spe_blog/plugins/issue_sidebar_single.html', 'Subscribe & read issue'),
)

DEFAULT_EDITORIAL_TEMPLATE = 'spe_blog/plugins/editorial.html'
EDITORIAL_TEMPLATES = (
    (DEFAULT_EDITORIAL_TEMPLATE, 'Editorial'),
)

DEFAULT_BRIEF_TEMPLATE = 'spe_blog/plugins/brief_interest.html'
BRIEF_TEMPLATES = (
    ('spe_blog/plugins/brief_index.html', 'Index listing'),
    ('spe_blog/plugins/brief_accordion.html', 'POI Accordion Listing'),
    ('spe_blog/plugins/side_list.html', 'Brief List'),
    ('spe_blog/plugins/best_shot_1.html', 'Best Shot 1 Col'),
    ('spe_blog/plugins/best_shot_2.html', 'Best Shot 2 Col'),
    ('spe_blog/plugins/best_shot.html', 'Best Shot 3 Col'),
    (DEFAULT_BRIEF_TEMPLATE, 'Brief of interest listing'),
)

DEFAULT_TOPIC_TEMPLATE = 'spe_blog/plugins/topics_list_3col.html'
TOPIC_TEMPLATES = (
    ('spe_blog/plugins/topics_list_1col.html', 'Topic List 1 Column'),
    ('spe_blog/plugins/topics_list.html', 'Topic List 2 Column'),
    (DEFAULT_TOPIC_TEMPLATE, 'Topic List 3 Column'),
)
DEFAULT_BOX_WIDTH = 'col-md-4'
BOX_WIDTH = (
    ('col-md-12', '1 Full Width Column'),
    ('col-md-6', '2 Column Format'),
    (DEFAULT_BOX_WIDTH, '3 Column Format'),
    ('col-md-3', '4 Column Format'),
)
DEFAULT_BOX_HEIGHT = 300
BOX_HEIGHT = (
    (DEFAULT_BOX_HEIGHT, 'Short Box'),
    (400, 'Medium Box'),
    (500, 'Tall Box'),
)


class ColorField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        super(ColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = ColorPickerWidget
        return super(ColorField, self).formfield(**kwargs)


class Article_Tagged(TaggedItemBase):
    content_object = models.ForeignKey("Article")


class Article_TaggedAuto(TaggedItemBase):
    content_object = models.ForeignKey("Article")


class Brief_Tagged(TaggedItemBase):
    content_object = models.ForeignKey("Brief")


class Brief_TaggedAuto(TaggedItemBase):
    content_object = models.ForeignKey("Brief")


class ArticleDetailPage(models.Model):
    name = models.CharField(max_length=150, unique=True)
    url = PageField(verbose_name="URL for article detail page", blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name


class BriefDetailPage(models.Model):
    name = models.CharField(max_length=150, unique=True)
    url = PageField(verbose_name="URL for brief detail page", blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name


class TopicsPage(models.Model):
    name = models.CharField(max_length=150, unique=True)
    url = PageField(verbose_name="URL for topics page", blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name


class TagsPage(models.Model):
    name = models.CharField(max_length=150, unique=True)
    url = PageField(verbose_name="URL for tags page", blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name


class Publication(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=150, unique=True)
    subscription_url = models.URLField(verbose_name=u'Subscription URL', blank=True, null=True)
    article_url = models.ForeignKey(ArticleDetailPage, verbose_name="URL for article detail page", blank=True,
                                    null=True, on_delete=models.SET_NULL)
    brief_url = models.ForeignKey(BriefDetailPage, verbose_name="URL for brief detail page", blank=True, null=True,
                                  on_delete=models.SET_NULL)
    topics_url = models.ForeignKey(TopicsPage, verbose_name="URL for topics page", blank=True, null=True,
                                   on_delete=models.SET_NULL)
    tags_url = models.ForeignKey(TagsPage, verbose_name="URL for tags page", blank=True, null=True,
                                 on_delete=models.SET_NULL)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.code + ": " + self.name

    def get_absolute_topics_url(self):
        if self.topics_url:
            page = Page.objects.get(pk=self.topics_url.url.id)
            url = page.get_absolute_url()
        else:
            url = ''
        return url


class Issue(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.PROTECT)
    date = models.DateField(verbose_name='Publication Date', blank=True, null=True)
    print_volume = models.PositiveIntegerField(blank=True, null=True)
    print_issue = models.PositiveIntegerField(blank=True, null=True)
    cover = FilerImageField(blank=True, null=True, verbose_name=u'Cover', related_name="cover_picture")
    coverblurb = models.TextField(verbose_name='Cover Description', max_length=1000, blank=True, null=True)
    covercredit = models.CharField(max_length=1000, blank=True, null=True)
    # issue_url = models.URLField(blank=True, null=True)
    issue_page = PageField(blank=True, null=True, on_delete=models.SET_NULL)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date', 'publication']

    def __unicode__(self):
        # return self.publication.name
        buf = self.publication.name
        if self.print_volume:
            buf += ": " + str(self.print_volume)
        if self.print_issue:
            buf += "-" + str(self.print_issue)
        if self.date:
            buf += " :: " + self.date.strftime("%B") + " " + str(self.date.year)
        return buf

    def get_absolute_url(self):
        if self.issue_page:
            url = self.issue_page.get_absolute_url()
        else:
            url = ''
        return url


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Category")

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.name


class SecondaryCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Category (Secondary)")

    class Meta:
        verbose_name_plural = "Categories (Secondary)"

    def __unicode__(self):
        return self.name


class Article(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.PROTECT)
    print_volume = models.PositiveIntegerField(blank=True, null=True)
    print_issue = models.PositiveIntegerField(blank=True, null=True)
    sponsored = models.BooleanField(default=False)
    free = models.BooleanField(default=False, verbose_name=u'Always Free')
    free_start = models.DateField(verbose_name='Start Date', blank=True, null=True)
    free_stop = models.DateField(verbose_name='End Date', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)
    secondary_category = models.ForeignKey(SecondaryCategory, on_delete=models.PROTECT, blank=True, null=True, verbose_name="Category (Secondary)")
    # categories = models.ManyToManyField(Category, blank=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100,
                            help_text='SEO Friendly name that is unique for use in URL', )
    teaser = models.CharField(max_length=300)
    author = models.CharField(max_length=500, blank=True, null=True)
    introduction = RichTextUploadingField(blank=True, null=True,
                                          help_text=u'Introductory paragraph or \'teaser.\' for paywal')
    article_text = RichTextUploadingField(
        max_length=50000,
        help_text=u'Full text of the article.'
    )
    date = models.DateField(verbose_name='Publication Date', default=timezone.now)
    #    discipline = models.CharField(max_length = 4, choices=DISCIPLINES)
    picture = FilerImageField(blank=True, null=True, verbose_name=u'Picture for article',
                              related_name="article_picture")
    picture_alternate = models.CharField(max_length=50, blank=True, null=True, verbose_name=u'Picture alternate text')
    picture_caption = models.CharField(max_length=300, blank=True, null=True, verbose_name=u'Picture caption')
    picture_attribution = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'Picture attribution')
    article_hits = models.PositiveIntegerField(default=0, editable=False)
    article_last_viewed = models.DateTimeField(blank=True, null=True, editable=False)
    disciplines = models.ManyToManyField(Tier1Discipline, blank=True)
    topics = models.ManyToManyField(Topics, verbose_name="Topics of Interest", blank=True)
    # add taggit tags, auto-tags, and categories

    tags = TaggableManager(verbose_name="Tags", through=Article_Tagged, blank=True)
    tags.rel.related_name = "+"
    auto_tags = TaggableManager(verbose_name="Auto Tags", through=Article_TaggedAuto, blank=True)
    auto_tags.rel.related_name = "+"
    published = models.BooleanField(default=False, verbose_name=u'Publish')

    # additional metohs for the editorials
    editorial_title = models.CharField(max_length=100, blank=True, null=True)
    author_picture = FilerImageField(blank=True, null=True, verbose_name=u'Picture for author',
                                     related_name="editorial_author_picture")
    # author_picture_alternate = models.CharField(max_length=50, blank=True, null=True,
    #                                             verbose_name=u'Author Picture Alternate Text')
    # author_picture_caption = models.CharField(max_length=250, blank=True, null=True,
    #                                           verbose_name=u'Author Picture Caption')
    author_picture_attribution = models.CharField(max_length=255, blank=True, null=True,
                                                  verbose_name=u'Author Picture Attribution')
    author_bio = RichTextField(
        max_length=500,
        help_text=u'Author Bio', blank=True, null=True
    )

    class Meta:
        unique_together = ('publication', 'print_volume', 'print_issue', 'slug', 'date')
        ordering = ['-date', 'title']
        get_latest_by = ['date']
        verbose_name = "article"

    def __unicode__(self):
        buf = ""
        if self.print_volume:
            buf = " " + str(self.print_volume)
        if self.print_issue:
            buf += ", " + str(self.print_issue)
        # buf = self.publication.code + buf + ": " + str(self.title)
        buf = self.publication.code + buf + ": " + unicode(self.title)
        if self.published:
            buf += " (PUBLISHED)"
        return buf

    def get_absolute_url(self):
        if self.publication.article_url:
            page = Page.objects.get(pk=self.publication.article_url.url.id)
            url = page.get_absolute_url() + "?art=" + str(self.id)
        else:
            url = reverse('article_detail', kwargs={'article_id': self.id})
        return url

    def is_readable(self):
        now = timezone.now().date()
        if self.free is True:
            return True
        if self.free_start is None and self.free_stop is None:
            return False
        if self.free_start is None or self.free_start <= now:
            if self.free_stop is None:
                return True
            if self.free_stop >= now:
                return True
        # here will go logic for membership viewing rights
        return False

    def show_paybox(self):
        now = timezone.now().date()
        if self.free:
            return False
        if self.free_start is None and self.free_stop is None:
            return False
        if self.free_start is None or self.free_start <= now:
            if self.free_stop is None:
                return True
            if self.free_stop >= now:
                return True
        return False


class Brief(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.PROTECT)
    print_volume = models.PositiveIntegerField(blank=True, null=True)
    print_issue = models.PositiveIntegerField(blank=True, null=True)
    free = models.BooleanField(default=True, verbose_name=u'Always Free')
    free_start = models.DateField(verbose_name='Start Date', blank=True, null=True)
    free_stop = models.DateField(verbose_name='End Date', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)
    secondary_category = models.ForeignKey(SecondaryCategory, on_delete=models.PROTECT, blank=True, null=True, verbose_name="Category (Secondary)")
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100,
                            help_text='SEO Friendly name that is unique for use in URL', )
    author = models.CharField(max_length=500, blank=True, null=True)
    article_text = RichTextUploadingField(
        max_length=50000,
        help_text=u'Full text of the article.'
    )
    date = models.DateField(verbose_name='Publication Date', default=timezone.now)
    picture = FilerImageField(blank=True, null=True, verbose_name=u'Picture for brief', related_name="brief_picture")
    picture_alternate = models.CharField(max_length=50, blank=True, null=True, verbose_name=u'Picture alternate text')
    article_hits = models.PositiveIntegerField(default=0, editable=False)
    article_last_viewed = models.DateTimeField(blank=True, null=True, editable=False)
    topics = models.ManyToManyField(Topics, verbose_name="Topics of Interest", blank=True)
    # add taggit tags, auto-tags, and categories
    tags = TaggableManager(verbose_name="Tags", through=Brief_Tagged, blank=True)
    tags.rel.related_name = "+"
    auto_tags = TaggableManager(verbose_name="Auto Tags", through=Brief_TaggedAuto, blank=True)
    auto_tags.rel.related_name = "+"
    published = models.BooleanField(default=False, verbose_name=u'Publish')

    class Meta:
        unique_together = ('publication', 'print_volume', 'print_issue', 'slug', 'date')
        ordering = ['-date', 'title']
        get_latest_by = ['date']
        verbose_name = "brief"

    def __unicode__(self):
        buf = ""
        if self.print_volume:
            buf = " " + str(self.print_volume)
        if self.print_issue:
            buf += ", " + str(self.print_issue)
        buf = self.publication.code + buf + ": " + unicode(self.title)
        if self.published:
            buf += " (PUBLISHED)"
        return buf

    def get_absolute_url(self):
        if self.publication.brief_url:
            page = Page.objects.get(pk=self.publication.brief_url.url.id)
            url = page.get_absolute_url() + "?art=" + str(self.id)
        else:
            url = reverse('brief_detail', kwargs={'brief_id': self.id})
        return url

    def is_readable(self):
        now = timezone.now().date()
        if self.free is True:
            return True
        if self.free_start is None and self.free_stop is None:
            return False
        if self.free_start is None or self.free_start <= now:
            if self.free_stop is None:
                return True
            if self.free_stop >= now:
                return True
        # here will go logic for membership viewing rights
        return False

    def show_paybox(self):
        now = timezone.now().date()
        if self.free:
            return False
        if self.free_start is None and self.free_stop is None:
            return False
        if self.free_start is None or self.free_start <= now:
            if self.free_stop is None:
                return True
            if self.free_stop >= now:
                return True
        return False


class Editorial(models.Model):
    title_main = models.CharField(max_length=100, verbose_name="Main Title")
    title_sub = models.CharField(max_length=100, verbose_name="Sub-Title")
    exerpt = RichTextField(
        max_length=300,
        help_text=u'Exerpt'
    )
    picture = FilerImageField(blank=True, null=True, verbose_name=u'Picture for editorial',
                              related_name="editorial_picture")
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
    #   keep_original_order = models.BooleanField(default=False)
    order_by = models.CharField(
        max_length=20,
        choices=ORDER_BY,
        default=DEFAULT_ORDER_BY,
        verbose_name="Otherwise order by"
    )
    # if user enters url and text then we display the show all link with these values
    # todo - change charfield to our URLField that takes relative paths
    all_url = PageField(verbose_name="URL for article listing page", blank=True, null=True, on_delete=models.SET_NULL)
    all_text = models.CharField("Show All Text", max_length=50, blank=True, null=True)
    backcol = ColorField("Background Color (for editorials only)", blank=True, null=True)
    fixedheight = models.BooleanField("Fixed Height", default=True)
    whitetext = models.BooleanField("White Text", default=True)
    boxwidth = models.CharField("TWA Article Box Width", max_length=10, choices=BOX_WIDTH, default=DEFAULT_BOX_WIDTH)
    boxheight = models.PositiveIntegerField("TWA Article Box Height", choices=BOX_HEIGHT, default=DEFAULT_BOX_HEIGHT)

    def __unicode__(self):
        #        if self.keep_original_order:
        #            buf = "Unordered"
        #        else:
        #            buf = self.get_order_by_display()
        #        buf = buf + u" (%s)" % ', '.join([a.slug for a in self.articles.all()])
        buf = self.get_order_by_display() + u" (%s)" % ', '.join([a.slug for a in self.articles.all()])
        return buf

    def copy_relations(self, old_instance):
        self.articles = old_instance.articles.all()


class BriefPlugin(CMSPlugin):
    template = models.CharField(max_length=255, choices=BRIEF_TEMPLATES, default=DEFAULT_BRIEF_TEMPLATE)
    briefs = models.ManyToManyField(Brief)
    order_by = models.CharField(
        max_length=20,
        choices=ORDER_BY,
        default=DEFAULT_ORDER_BY,
        verbose_name="Otherwise order by"
    )
    # if user enters url and text then we display the show all link with these values
    # todo - change charfield to our URLField that takes relative paths
    all_url = PageField(verbose_name="URL for briefs listing page", blank=True, null=True, on_delete=models.SET_NULL)
    all_text = models.CharField("Show All Text", max_length=50, blank=True, null=True)
    backcol = ColorField("Background Color", blank=True, null=True)
    whitetext = models.BooleanField("White Text", default=True)

    def __unicode__(self):
        buf = self.get_order_by_display() + u" (%s)" % ', '.join([b.slug for b in self.briefs.all()])
        return buf

    def copy_relations(self, old_instance):
        self.briefs = old_instance.briefs.all()


class ArticleDetailPlugin(CMSPlugin):
    allow_url_to_override_selection = models.BooleanField(default=False)
    article = models.ForeignKey(Article, verbose_name="Selected article (default)", on_delete=models.PROTECT)
    show_related_articles = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.article.publication.code) + ": " + self.article.title


class TopicsPlugin(CMSPlugin):
    allow_url_to_override_selection = models.BooleanField(default=False)
    publication = models.ForeignKey(Publication, on_delete=models.PROTECT)
    template = models.CharField(max_length=255, choices=PLUGIN_TEMPLATES, default=DEFAULT_PLUGIN_TEMPLATE)
    cnt = models.PositiveIntegerField(default=5, verbose_name=u'Number of Articles')
    order_by = models.CharField(max_length=20, choices=ORDER_BY, default=DEFAULT_ORDER_BY)
    starting_with = models.PositiveIntegerField(default=1)
    topics = models.ManyToManyField(Topics, verbose_name="Topics of Interest", blank=True)

    def __unicode__(self):
        dictionary = dict(PLUGIN_TEMPLATES)
        buf = "(" + str(self.starting_with) + " - " + str(
            self.cnt + self.starting_with - 1) + ") by " + self.get_order_by_display()
        buf += " using " + dictionary[self.template]  # + " - "
        # buf += u" (%s)" % ', '.join([a.topics.name for a in self.topics.all()])
        return buf

    def copy_relations(self, old_instance):
        self.topics = old_instance.topics.all()


class TopicsListPlugin(CMSPlugin):
    template = models.CharField(max_length=255, choices=TOPIC_TEMPLATES, default=DEFAULT_TOPIC_TEMPLATE)
    topics = models.ManyToManyField(Topics, verbose_name="Topics of Interest", blank=True)
    publication = models.ForeignKey(Publication, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        dictionary = dict(TOPIC_TEMPLATES)
        return self.publication.code + ": " + dictionary[self.template]

    def copy_relations(self, old_instance):
        self.topics = old_instance.topics.all()


class BriefDetailPlugin(CMSPlugin):
    allow_url_to_override_selection = models.BooleanField(default=False)
    brief = models.ForeignKey(Brief, on_delete=models.PROTECT)

    def __unicode__(self):
        return str(self.brief.publication.code) + ": " + self.brief.title


class EditorialPlugin(CMSPlugin):
    template = models.CharField(max_length=255, choices=EDITORIAL_TEMPLATES, default=DEFAULT_EDITORIAL_TEMPLATE)
    editorial = models.ManyToManyField(Editorial)
    lnk = models.URLField("Link URL", blank=True, null=True)
    backcol = ColorField("Background Color", blank=True, null=True)

    def __unicode__(self):
        return "Editorial Plugin"

    def copy_relations(self, old_instance):
        self.editorial = old_instance.editorial.all()


class ArticlesListingPlugin(CMSPlugin):
    # display
    template = models.CharField(max_length=255, choices=PLUGIN_TEMPLATES, default=DEFAULT_PLUGIN_TEMPLATE)
    backcol = ColorField("Background Color (for editorials only.)", blank=True, null=True)
    cnt = models.PositiveIntegerField(default=5, verbose_name=u'Number of Articles')
    order_by = models.CharField(max_length=20, choices=ORDER_BY, default=DEFAULT_ORDER_BY)
    starting_with = models.PositiveIntegerField(default=1)
    # limit to
    publication = models.ForeignKey(Publication, blank=True, null=True, on_delete=models.SET_NULL)
    print_volume = models.PositiveIntegerField(blank=True, null=True)
    print_issue = models.PositiveIntegerField(blank=True, null=True)
    personalized = models.BooleanField(default=False)
    discipline = models.ForeignKey(Tier1Discipline, blank=True, null=True, on_delete=models.SET_NULL)
    # category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    categories = models.ManyToManyField(Category, blank=True)
    secondary_categories = models.ManyToManyField(SecondaryCategory, blank=True)
    # if user enters url and text then we display the show all link with these values
    all_url = PageField(verbose_name="URL for article listing page", blank=True, null=True, on_delete=models.SET_NULL)
    all_text = models.CharField("Show All Text", max_length=50, blank=True, null=True)
    backcol = ColorField("Background Color (.for editorials only.)", blank=True, null=True)
    fixedheight = models.BooleanField("Fixed Height", default=True)
    whitetext = models.BooleanField("White Text", default=True)
    boxwidth = models.CharField("TWA Article Box Width", max_length=10, choices=BOX_WIDTH, default=DEFAULT_BOX_WIDTH)
    boxheight = models.PositiveIntegerField("TWA Article Box Height", choices=BOX_HEIGHT, default=DEFAULT_BOX_HEIGHT)

    def __unicode__(self):
        dictionary = dict(PLUGIN_TEMPLATES)
        buf = "(" + str(self.starting_with) + " - " + str(
            self.cnt + self.starting_with - 1) + ") by " + self.get_order_by_display()
        if self.discipline:
            buf += " (" + self.discipline.code + ")"
        if self.personalized:
            buf += " personalized"
        # if self.category:
        #     buf += " (" + self.category.name + " only)"
        buf += " using " + dictionary[self.template]
        return buf

    def copy_relations(self, old_instance):
        self.categories = old_instance.categories.all()
        self.secondary_categories = old_instance.secondary_categories.all()


class BriefListingPlugin(CMSPlugin):
    template = models.CharField(max_length=255, choices=BRIEF_TEMPLATES, default=DEFAULT_BRIEF_TEMPLATE)
    cnt = models.PositiveIntegerField(default=5, verbose_name=u'Number of Briefs')
    order_by = models.CharField(max_length=20, choices=ORDER_BY, default=DEFAULT_ORDER_BY)
    starting_with = models.PositiveIntegerField(default=1)
    # limit to
    publication = models.ForeignKey(Publication, blank=True, null=True, on_delete=models.SET_NULL)
    print_volume = models.PositiveIntegerField(blank=True, null=True)
    print_issue = models.PositiveIntegerField(blank=True, null=True)
    # category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    categories = models.ManyToManyField(Category, blank=True)
    secondary_categories = models.ManyToManyField(SecondaryCategory, blank=True)
    topic = models.ForeignKey(Topics, blank=True, null=True, on_delete=models.SET_NULL)
    # if user enters url and text then we display the show all link with these values
    all_url = PageField(verbose_name="URL for briefs listing page", blank=True, null=True, on_delete=models.SET_NULL)
    all_text = models.CharField("Show All Text", max_length=50, blank=True, null=True)
    backcol = ColorField("Background Color", blank=True, null=True)
    whitetext = models.BooleanField("White Text", default=True)

    def __unicode__(self):
        dictionary = dict(BRIEF_TEMPLATES)
        buf = "(" + str(self.starting_with) + " - " + str(
            self.cnt + self.starting_with - 1) + ") by " + self.get_order_by_display()
        # if self.category:
        #     buf += " (" + self.category.name + " only)"
        if self.topic:
            buf += " (" + self.topic.name + " only)"
        buf += " using " + dictionary[self.template]
        return buf

    def copy_relations(self, old_instance):
        self.categories = old_instance.categories.all()


class IssuesByPublicationPlugin(CMSPlugin):
    template = models.CharField(max_length=255, choices=ISSUE_TEMPLATES, default=DEFAULT_ISSUE_TEMPLATE)
    cnt = models.PositiveIntegerField(default=5, verbose_name=u'Number of Issues')
    starting_with = models.PositiveIntegerField(default=1)
    publication = models.ForeignKey(Publication, on_delete=models.PROTECT)
    active = models.BooleanField(default=True)
    all_url = PageField(verbose_name="URL for issues listing page", blank=True, null=True, on_delete=models.SET_NULL)
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


class BreadCrumbPlugin(CMSPlugin):
    title = models.CharField(max_length=50)

    def __unicode__(self):
        return self.title


class IssuesByYearPlugin(CMSPlugin):
    publication = models.ForeignKey(Publication, on_delete=models.PROTECT)

    def __unicode__(self):
        return self.publication.name


class IssueCoverPlugin(CMSPlugin):
    template = models.CharField(max_length=255, choices=ISSUECOVER_TEMPLATES, default=DEFAULT_ISSUECOVER_TEMPLATE)
    publication = models.ForeignKey(Publication, on_delete=models.PROTECT)
    issue = models.ForeignKey(Issue, on_delete=models.PROTECT)
    all_url = PageField(verbose_name="URL for Issue Page", blank=True, null=True, on_delete=models.SET_NULL)
    all_text = models.CharField("More Items Link", max_length=50, blank=True, null=True)

    def __unicode__(self):
        dictionary = dict(ISSUECOVER_TEMPLATES)
        buf = dictionary[self.template]
        buf += " || Pub: " + self.publication.name
        buf += " || Issue: " + str(self.issue.print_volume) + "-" + str(self.issue.print_issue)
        return buf


class TagsDetailPlugin(CMSPlugin):
    publication = models.ForeignKey(Publication, on_delete=models.PROTECT)
    template = models.CharField(max_length=255, choices=PLUGIN_TEMPLATES, default=DEFAULT_PLUGIN_TEMPLATE)
    cnt = models.PositiveIntegerField(default=5, verbose_name=u'Number of Articles')
    order_by = models.CharField(max_length=20, choices=ORDER_BY, default=DEFAULT_ORDER_BY)
    starting_with = models.PositiveIntegerField(default=1)

    def __unicode__(self):
        dictionary = dict(PLUGIN_TEMPLATES)
        buf = "(" + str(self.starting_with) + " - " + str(
            self.cnt + self.starting_with - 1) + ") by " + self.get_order_by_display()
        buf += " using " + dictionary[self.template]  # + " - "
        # buf += u" (%s)" % ', '.join([a.topics.name for a in self.topics.all()])
        return buf
