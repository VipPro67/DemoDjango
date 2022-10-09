from re import template
from tempfile import tempdir
from django. http import HttpResponse
from django.template import loader
def index(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())