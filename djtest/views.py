# coding=utf8
from page.models import Poll
from django.template import loader, Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse

def hello(request):
	return HttpResponse("Hello World")

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    t = loader.get_template('page/index.html')
    c = Context({
        'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(t.render(c));

def detail(request, poll_id):
    try:
        p = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response('page/details.html',
        {'poll': p},
        )

def results(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('page/results.html', {'poll':p},
        context_instance=RequestContext(request))

def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    try:
        choice = poll.choice_set.get(pk=request.POST['choice'])
    except:
        return render_to_response('page/details.html', {'poll':poll, 'error_message':u'您选择的选项不存在'})
    else:
        choice.votes += 1
        choice.save()
        return HttpResponseRedirect('/page/'+str(poll.id))
