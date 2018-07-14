from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse

from django.contrib.contenttypes.models import ContentType

from django.db.models.signals import pre_save
from django.utils.text import slugify

from comments.models import Comment


class Wiki(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(max_length=20000, blank=True, null=True)
    history = models.TextField(max_length=20000, blank=True, null=True)
    features = models.TextField(max_length=20000, blank=True, null=True)
    version_history = models.TextField(max_length=20000, blank=True, null=True)
    url = models.TextField(max_length=5000,null=True,blank=True)
    tech_name = models.CharField(max_length=100, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    eli = models.TextField(max_length=20000, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    tags = models.ManyToManyField('tags.Tag', related_name='wiki_pages', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("wiki:wiki_details", kwargs={"slug" : self.slug})

    class Meta:
        ordering = ["-timestamp" , "-last_updated"]

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)

    if new_slug is not None:
        slug = new_slug
    qs = Wiki.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()

    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

# signal receiver
def pre_save_wiki_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
pre_save.connect(pre_save_wiki_receiver, sender=Wiki)


class Resources(models.Model):
    user = models.ForeignKey(User)
    wiki = models.CharField(max_length=20000)
    title = models.CharField(max_length=20000, unique=True)
    link = models.URLField(null=True, blank=True)
    resource = models.TextField(max_length=20000)
    date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-date"]
