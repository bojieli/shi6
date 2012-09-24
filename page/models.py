# coding=utf8
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Article(models.Model):
    author      = models.ForeignKey(User)
    create_time = models.DateField(db_index=True)
    last_modified_time = models.DateField(db_index=True)
    permission  = models.IntegerField(default=0)
    title       = models.CharField(max_length=255)
    text        = models.TextField()
    isdeleted   = models.BooleanField(default=False)
    delete_time = models.DateField()
admin.site.register(Article)

class ArticleFile(models.Model):
    article     = models.ForeignKey(Article)
    file        = models.OneToOneField('core.File')
admin.site.register(ArticleFile)

class Comment(models.Model):
    article     = models.ForeignKey(Article)
    parent      = models.ForeignKey('self', null=True, blank=True)
    author      = models.ForeignKey(User)
    create_time = models.DateField(db_index=True)
    text        = models.TextField()
    isdeleted   = models.BooleanField(default=False)
    delete_time = models.DateField()
admin.site.register(Comment)

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()

    def __unicode__(self):
        return self.choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['question']}),
        (u'日期', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'

admin.site.register(Poll, PollAdmin)
