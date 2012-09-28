from django.contrib import admin

def add_admin(c):
    admin.site.register(c)
    return c
