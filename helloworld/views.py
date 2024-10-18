from django.http import HttpResponse

def response(request):
    res = "<h1>Hello world Django</h1>"
    return HttpResponse(res)