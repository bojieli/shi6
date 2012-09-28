# coding=utf8
from django.db import models
from django.contrib.auth.models import User
from core.models import FileList
from django.contrib import admin
import utils

@utils.add_admin
class Article(models.Model):
    author      = models.ForeignKey(User)
    create_time = models.DateField(db_index=True)
    last_modified_time = models.DateField(db_index=True)
    permission  = models.IntegerField(default=0)
    title       = models.CharField(max_length=255)
    text        = models.TextField()
    isdeleted   = models.BooleanField(default=False)
    delete_time = models.DateField()
    filelist    = models.OneToOneField(FileList, null=True, blank=True)

@utils.add_admin
class Comment(models.Model):
    article     = models.ForeignKey(Article)
    parent      = models.ForeignKey('self', null=True, blank=True)
    author      = models.ForeignKey(User)
    create_time = models.DateField(db_index=True)
    text        = models.TextField()
    isdeleted   = models.BooleanField(default=False)
    delete_time = models.DateField()
