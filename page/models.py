# coding=utf8
from django.db import models
from django.contrib.auth.models import User
from core.models import FileList
from django.contrib import admin
import utils

@utils.addAdmin
class CommentList(models.Model):
    pass

@utils.addAdmin
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
    commentList = models.ForeignKey(CommentList)

@utils.addAdmin
class Message(models.Model):
    author      = models.ForeignKey(User)
    create_time = models.DateField(db_index=True)
    last_modified_time = models.DateField(db_index=True)
    permission  = models.IntegerField(default=0)
    text        = models.TextField()
    isdeleted   = models.BooleanField(default=False)
    delete_time = models.DateField()
    commentList = models.ForeignKey(CommentList)

@utils.addAdmin
class Comment(models.Model):
    root        = models.ForeignKey(CommentList)
    parent      = models.ForeignKey('self', null=True, blank=True)
    author      = models.ForeignKey(User)
    create_time = models.DateField(db_index=True)
    text        = models.TextField()
    isdeleted   = models.BooleanField(default=False)
    delete_time = models.DateField()
