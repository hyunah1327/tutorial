from django.http import HttpResponse


from django.http import HttpResponse

def home(request):
    return HttpResponse('Home')