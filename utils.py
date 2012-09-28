from django.contrib import admin

def addAdmin(c):
    admin.site.register(c)
    return c
