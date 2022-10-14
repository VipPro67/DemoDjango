from re import template
from tempfile import tempdir
from django. http import HttpResponse
from django.template import loader
def index(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
def index2(request):
    template = loader.get_template('uudiem_hanche.html')
    return HttpResponse(template.render())
def index3(request):
    template = loader.get_template('django_vs_nodeJs.html')
    return HttpResponse(template.render())
def index4(request):
    template = loader.get_template('GiaiQuyet.html')
    return HttpResponse(template.render())
def index5(request):
    template = loader.get_template('LiDo.html')
    return HttpResponse(template.render())
def index6(request):
    template = loader.get_template('QuyTrinh.html')
    return HttpResponse(template.render())