# coding=utf8
from django.template import loader, Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse

def index(request):
	return HttpResponse("Hello World")
