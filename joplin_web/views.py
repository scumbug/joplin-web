from django.http import HttpResponse
from django.template.response import TemplateResponse


def base(request):
    html = TemplateResponse(request, 'index.html')
    return HttpResponse(html.render())
