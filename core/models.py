# coding=utf8
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class School(models.Model):
    name        = models.CharField(max_length=200, db_index=True)
    SCHOOL_TYPES = (
        ('DX', u'大学'),
        ('GZ', u'高中'),
        ('CZ', u'初中'),
        ('XX', u'小学'),
        ('QT', u'其他'),
    )
    type        = models.CharField(max_length=2, choices=SCHOOL_TYPES, db_index=True)
    city        = models.CharField(max_length=100, db_index=True)
admin.site.register(School)

class GroupCategory(models.Model):
    name        = models.CharField(max_length=200)
admin.site.register(GroupCategory)

class Group(models.Model):
    name        = models.CharField(max_length=200)
    school      = models.ForeignKey(School, null=True, blank=True)
    category    = models.ForeignKey(GroupCategory)
    creator     = models.ForeignKey(User, related_name='group_created')
    create_time = models.DateField(db_index=True)
    total_rate  = models.IntegerField(default=0, db_index=True)
    isdeleted   = models.BooleanField(default=False)
    delete_time = models.DateField()
    members     = models.ManyToManyField(User, through='Membership', related_name='group_joined')
admin.site.register(Group)

class GroupTag(models.Model):
    group       = models.ForeignKey(Group)
    tag         = models.CharField(max_length=200, db_index=True)
admin.site.register(GroupTag)

class File(models.Model):
    author      = models.ForeignKey(User)
    create_time = models.DateField(db_index=True)
    permission  = models.IntegerField(default=0)
    mimetype    = models.CharField(max_length=30)
    filename    = models.CharField(max_length=255)
    local_filename = models.CharField(max_length=100)
    isdeleted   = models.BooleanField(default=False)
    delete_time = models.DateField()
admin.site.register(File)

class FileList(models.Model):
    pass
admin.site.register(FileList)

class Image(models.Model):
    original_image = models.OneToOneField(File)
admin.site.register(Image)

class Thumb(models.Model):
    image = models.ForeignKey(Image)
    file  = models.OneToOneField(File)
admin.site.register(Thumb)

class GroupProfile(models.Model):
    group       = models.OneToOneField(Group)
    name_en     = models.CharField(max_length=200)
    slogan      = models.CharField(max_length=200)
    email       = models.CharField(max_length=200)
    logo        = models.ForeignKey(Image)
    summary     = models.TextField()
    description = models.TextField()

class Membership(models.Model):
    group       = models.ForeignKey(Group)
    user        = models.ForeignKey(User)
    PRIVILEGE_CHOICES = (
        (0, u'admin'),
        (1, u'manager'),
        (2, u'member'),
        (3, u'inactive')
    )
    privilege   = models.IntegerField(choices=PRIVILEGE_CHOICES, db_index=True)
    title       = models.CharField(max_length=200)
admin.site.register(Membership)

class UserProfile(models.Model):
    user        = models.OneToOneField(User) 
    realname    = models.CharField(max_length=200, db_index=True)
    school      = models.ForeignKey(School)
    avatar      = models.OneToOneField(Image)
    student_no  = models.CharField(max_length=20)
    telephone   = models.CharField(max_length=20)
    EDUCATION_CHOICES = (
        ('PB', u'本科'),
        ('SA', u'硕士'),
        ('BA', u'博士'),
        ('JL', u'交流'),
        ('GZ', u'高中'),
        ('CZ', u'初中'),
        ('XX', u'小学'),
        ('QT', u'其他'),
    )
    education   = models.CharField(max_length=2, choices=EDUCATION_CHOICES, db_index=True)
    admission_year = models.IntegerField(db_index=True)
    dept        = models.CharField(max_length=200, db_index=True)
    major       = models.CharField(max_length=200, db_index=True)
    ps          = models.TextField()
admin.site.register(UserProfile)

class UserLoginLog(models.Model):
    ip          = models.CharField(max_length=50, db_index=True)
    time        = models.DateField(db_index=True)
    LOGIN_METHODS = (
        ('16', u'本地注册'),
        ('RR', u'人人网'),
        ('QQ', u'腾讯QQ'),
        ('WB', u'新浪微博'),
        ('BD', u'百度'),
        ('GG', u'Google'),
        ('FB', u'Facebook'),
        ('TW', u'Twitter'),
    )
    method      = models.CharField(max_length=2, choices=LOGIN_METHODS)
    user        = models.ForeignKey(User, null=True, blank=True)
    result      = models.BooleanField()
admin.site.register(UserLoginLog)

admin.site.register(User)

